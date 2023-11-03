import csv
from pathlib import Path

class Course():
    
    def __init__(self, name, enrollement, preferred, facilitators, others):
        
        self.name = name
        self.enrollment = enrollement
        self.preferred = preferred
        self.facilitators = facilitators
        self.others = others
        self.fitness = 0
    
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

    times_path = Path(r'Program 2\times.txt')
    rooms_path = Path(r'Program 2\rooms.csv')
    
    times = times_path.read_text().split('\n')
    rooms = {}
    
    with open(rooms_path) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        for row in csv_reader:
            
            rooms = row
    
main()