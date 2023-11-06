import json, pathlib
import numpy as np
from random import sample
from datetime import datetime
class Population():
    
    def __init__(self, courses, facilitators, times, rooms):
        
        self.schedule = []
        self.generations = []
        self.courses = courses
        self.facilitators = facilitators
        self.times = times
        self.rooms = rooms
        
        self.generate()
        
    def generate(self):
        
        for course in self.courses:
            
            room = sample(self.rooms, len(self.rooms))
            time = sample(self.times, len(self.times))
            facilitator = sample(self.facilitators, len(self.facilitators))
            
            activity = Activity(
                course, facilitator.pop(), time.pop(), room.pop()
                )
            self.schedule.append(activity)
        
        self.generations.append(self.schedule)
    
        for activity in self.schedule:
            
            self.get_fitness(activity)
        
    def get_fitness(self, activity):
        
        fitness = 0
        
        schedule = self.schedule.copy()
        schedule.remove(activity)
        
        name = activity.get_name()
        time = activity.get_time()
        room = activity.get_room()
        facilitator = activity.get_facilitator()
        
        for other in schedule:
            
            if activity.is_conflict(other): 
                
                fitness -= 0.5
                break
        
        # room size
        if activity.get_capacity() < activity.get_enrollment():
            
            fitness -= 0.5

        elif (activity.get_capacity() / activity.get_enrollment()) > 6: 
            
            fitness -= 0.4
            
        elif (activity.get_capacity() / activity.get_enrollment()) > 3: 
            
            fitness -= 0.2

        else: fitness += 0.3
        
        if activity.is_preferred():
            
            fitness += 0.5
            
        elif activity.is_other():
            
            fitness += 0.2
        
        else:
            
            fitness -= 0.1
        
        # facilator load
        conflicts = 0
        scheduled = 0
        
        for other in schedule:
            
            if time == other.get_time() and facilitator == other.get_facilitator():
                
                conflicts += 1
            
            if facilitator == other.get_facilitator:
                
                scheduled += 1
            
        else:
            if conflicts == 0: fitness += 0.2
            
            elif conflicts == 1: fitness -= 0.2
            
            elif conflicts > 4: fitness -= 0.5
        
            if scheduled > 2 and facilitator != 'Tyler': 
                
                fitness -= 0.4
        
        # activitiy-specific adjustments
        if name.startswith(('SLA100', 'SLA191')):
            
            other, = [
                other for other in schedule 
                if other.get_name()[:-1] == name[:-1]
                ]
            difference = time - other.get_time()
            difference = (difference.seconds / 60 / 60) % 12
            
            if difference > 4:
                
                fitness += 0.5
                
            if time == other.get_time():
                
                fitness -= 0.5
            
            if name.startswith('SLA100'):
                
                other, = [
                    other for other in schedule 
                    if other.get_name()[:-1] == 'SLA191'
                    ]

            elif name.startswith('SLA191'):
                
                other, = [
                    other for other in schedule 
                    if other.get_name()[:-1] == 'SLA100'
                    ]

            difference = time - other.get_time()
            difference = (difference.seconds / 60 / 60) % 12
            
            if difference == 1:
                
                if room.startswith(('Roman', 'Beach')) and room != other.get_room():
                    
                    fitness -= 0.4
                
                else:
                    
                    fitness += 0.5            
            
            if difference == 2: fitness += 0.25
            
            if time == other.get_time():
                
                fitness -= 0.25
        
        activity.set_fitness(fitness)
        
    def softmax(self):
       
       np.exp(x) / sum(np.exp(x))

class Activity():
    
    def __init__(self, course, facilitator, time, room):

        self.fitness = 0
        self.course = course
        self.facilitator = facilitator
        self.time = time
        self.room = room
        
    def __repr__(self):
        
        return f'{self.room} {self.course.name} — {datetime.strftime(self.time, "%I:%M %p")} {self.facilitator}'
            
    def set_fitness(self, fitness):
        
        self.fitness = fitness
    
    def get_name(self):
        
        return self.course.name
    
    def get_enrollment(self):
        
        return self.course.enrollment

    def get_capacity(self):
        
        return self.room.capacity
    
    def get_time(self):
        
        return self.time
    
    def get_room(self):
        
        return self.room()
    
    def is_conflict(self, other):
        
        if self == other: return False
        
        return self.time == other.time and self.room == other.room
        
    def is_preffered(self):
        
        return self.facilitator in self.preferred
    
    def is_other(self):
        
        return self.facilitator in self.other
        
class Course():
    
    def __init__(self, name, kwargs):
        
        self.name = name
        self.enrollment = kwargs['enrollment']
        self.preferred = kwargs['preferred']
        self.others = kwargs['others']
    
    def __repr__(self):
        
        return f'{self.name} ({self.enrollment})\nPreffered: {self.preferred}\nOthers: {self.others}'

    def compare(self, other):
        
        pass
        
    def get_enrollment(self):
        
        return self.enrollment
        
    def is_preffered(self, facilitator):
        
        return facilitator in self.preferred
    
    def is_other(self, facilitator):
        
        return facilitator in self.other

class Room():
    
    def __init__(self, name, capacity):
        
        self.name = name
        self.capacity = capacity
        
    def __repr__(self):
        
        return f'{self.name} ({self.capacity})'
    
    def get_capacity(self):
        
        return self.capacity
    
def main(): 

    data = json.load(open('Program 2\data.json'))
    report = pathlib.Path('Program 2\report.txt')
    courses = [
        Course(course, values) for course, values in data['courses'].items()
        ]
    facilitators = data['facilitators']
    times = [
        datetime.strptime(time, "%I:%M %p") for time in data['times']
        ]
    rooms = [
        Room(room, values) for room, values in data['rooms'].items()
        ]
    
    if report.exists(): report.touch()
    
    population = Population(courses, facilitators, times, rooms)
    
    while 0:
        population.generate()
    
main()