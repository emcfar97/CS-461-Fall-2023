import json

class Course():
    
    def __init__(self, name, kwargs):
        
        self.name = name
        self.enrollment = kwargs['enrollment']
        self.preferred = kwargs['preferred']
        self.others = kwargs['others']
        self.fitness = 0
    
    def __repr__(self):
        
        return f'{self.name} ({self.enrollment})\nPreffered: {self.preferred}\nOthers: {self.others}'
    
def fitness():
    
    if 0: -0.5
    if 1: -0.5    
    if 2: -0.2
    elif 3: -0.4
    else: 0.3
    if 5: 0.5
    if 6: 0.2
    if 7: -0.1
    if 8: 0.2
    if 9: -0.2
    if 10: -0.5
    if 11: -0.4
    
    if 1: 0.5
    if 2: -0.5
    if 3: 0.5
    if 4: -0.5
    if 5: 0.5
    if 6: -0.4
    if 7: 0.25
    if 8: -0.25

def main(): 

    data = json.load(open('Program 2\data.json'))
    courses = [
        Course(course, values) for course, values in data['courses'].items()
        ]
    facilitators = data['facilitators']
    times = data['times']
    rooms = data['rooms']
    
main()