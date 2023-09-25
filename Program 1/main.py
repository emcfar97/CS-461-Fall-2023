import csv, pathlib
from collections import defaultdict
from queue import PriorityQueue

class Graph:
    'This class represents a directed graph using adjacency list representation'
 
    def __init__(self):
        'Constructor'
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
    def addEdge(self, u, v):
        'Function to add an edge to graph'
        
        self.graph[u].append(v)
 
    def BFS(self, s):
        'Function to print a BFS of graph'
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")
 
            # Get all adjacent vertices of the dequeued vertex s.
            # If an adjacent has not been visited,
            # then mark it visited and enqueue it
            for i in self.graph[s]:
                
                if visited[i] == False:
                
                    queue.append(i)
                    visited[i] = True
            
class Graph:
    'This class represents a directed graph using adjacency list representation'
 
    def __init__(self):
        'Constructor'
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
 
     
    def addEdge(self, u, v):
        'Function to add an edge to graph'
        
        self.graph[u].append(v)
     
    def DFSUtil(self, v, visited):
        'A function used by DFS'
 
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            
            if neighbour not in visited:
                
                self.DFSUtil(neighbour, visited)
 
    def DFS(self, v):
        'The function to do DFS traversal. It uses recursive DFSUtil()'
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)

class Graph:
    'This class represents a directed graph using adjacency list representation'
    
    def __init__(self,vertices):
        'Constructor'
 
        # No. of vertices
        self.V = vertices
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    def addEdge(self,u,v):
        'function to add an edge to graph'
        
        self.graph[u].append(v)
 
    def DLS(self,src,target,maxDepth):
        'A function to perform a Depth-Limited search from given source "src"'
 
        if src == target : return True
 
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:

                if(self.DLS(i,target,maxDepth-1)):

                    return True

        return False
 
    def IDDFS(self,src, target, maxDepth):
        'IDDFS to search if target is reachable from v. It uses recursive DLS()'
 
        # Repeatedly depth-limit search till the maximum depth
        for i in range(maxDepth):
            
            if (self.DLS(src, target, i)):
            
                return True
            
        return False
            
towns_path = pathlib.Path(r'Program 1\coordinates.csv')
adjacencies_path = pathlib.Path(r'Program 1\Adjacencies.txt')

towns = csv.DictReader(towns_path)
adjacencies = adjacencies_path.read_text()

town = None

while town is None: # Sey starting and ending towns
    
    start_town = input(
        'Please choose a starting town: '
        )
    end_town = input(
        'Please choose a ending town: '
        )
    
    if start_town in towns and end_town in towns:
        
        town = [start_town, end_town]

    elif start_town not in towns and end_town in towns:
        
        print(f'Start town {start_town} is not in database. Please try again.')
        
    elif end_town not in towns and start_town in towns:
        
        print(f'End town {end_town} is not in database. Please try again.')
    else:
        
        print(
            f'Neither {start_town} or {end_town} are in database. Please try again.')
    
while True: # Main program
    
    user_input = input(
        'Choose from:\n1 - Undirected (blind) brute-force approach\n2 - Breadth-first search\n3 - Depth-first search\n4 - ID-DFS search\n5 - Best-first search\n6 - A* search\n7 - Exit\n'
        )
    
    if   user_input == '1': # Undirected (blind) brute-force approach
        
        pass
    
    elif user_input == '2': # Breadth-first search
    
        pass

    elif user_input == '3': # Depth-first search
    
        pass

    elif user_input == '4': # ID-DFS search
    
        pass

    elif user_input == '5': # Best-first search
    
        pass

    elif user_input == '6': # A* search
    
        pass

    elif user_input == '7': # Exit
    
        pass
