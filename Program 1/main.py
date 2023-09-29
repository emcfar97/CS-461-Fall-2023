import csv, pathlib, timeit
from math import dist
from collections import defaultdict, deque
from queue import PriorityQueue

class Graph:
    'This class represents a directed graph using adjacency list representation'
 
    def __init__(self, nodes, vertices):
        'Constructor'
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        
        # Populate graph
        for vertice in vertices:
            
            town_a, town_b = vertice.split()
            
            self.add_edge(nodes[town_a], nodes[town_b])
  
    def add_edge(self, u, v):
        'Function to add an edge to graph, with cost computed from Euclidean distance'
        
        self.graph[u].append((v, u % v))
    
    def clear_graph(self):
        'Mark all node as unvisted'
        
        for node in self.graph:
            
            node.visited = False
    
    def breadth_first_search(self, root):
        'Function to print a BFS of graph'
  
        # Create queues for visited and unvisited nodes
        visited, queue = set(), deque([root])
        visited.add(root)
 
        while queue:
 
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")

            # If not visited, mark it as visited, and enqueue it
            for neighbour in self.graph[vertex]:
                
                if neighbour not in visited:
                    
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        print()
        
    def DFSUtil(self, v, visited):
        'A function used by DFS'
 
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=' ')
 
        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            
            if neighbour not in visited:
                
                self.DFSUtil(neighbour, visited)
 
    def depth_first_search(self, v):
        'The function to do DFS traversal. It uses recursive DFSUtil()'
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(v, visited)
 
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
 
    def ID_DFS(self,src, target, maxDepth):
        'ID-DFS to search if target is reachable from v. It uses recursive DLS()'
 
        # Repeatedly depth-limit search till the maximum depth
        for i in range(maxDepth):
            
            if (self.DLS(src, target, i)):
            
                return True
            
        return False
    
    def best_first_search(self, actual_Src, target, n):
        'Function to print a BFS of graph'

        self.graph = [[] for i in range(v)]
        visited = [False] * n
        pq = PriorityQueue()
        pq.put((0, actual_Src))
        visited[actual_Src] = True
        
        while pq.empty() == False:

            u = pq.get()[1]
            # Displaying the path having lowest cost
            print(u, end=" ")

            if u == target:

                break
    
            for v, c in self.graph[u]:

                if visited[v] == False:

                    visited[v] = True
                    pq.put((c, v))
        print()
    
    def astar(maze, start, end):
        'Returns a list of tuples as a path from the given start to the given end in the given maze'

        # Create start and end node
        start_node = Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:

            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1] # Return reversed path

            # Generate children
            children = []
            for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if maze[node_position[0]][node_position[1]] != 0:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                for closed_child in closed_list:
                    if child == closed_child:
                        continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

class Town():
    'Town class for Graph'
    
    def __init__(self, name, position):
        
        self.name = name
        self.position = position
        self.vistited = False
    
    def __repr__(self): return f'{self.name} {self.position}'
    
    def __mod__(self, other): return dist(self.position, other.position)
    
    def set_visited(self): self.visited = not self.visited
    
    def get_visited(self): return self.visited
    
class Node():
    'Node class for A* Pathfinding'

    def __init__(self, parent=None, position=None):
        
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        
        return self.position == other.position

towns_path = pathlib.Path(r'Program 1\coordinates.csv')
adjacencies_path = pathlib.Path(r'Program 1\Adjacencies.txt')
towns = {}

with open(towns_path) as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        
        towns[row[0]] = Town(row[0], (float(row[1]), float(row[2])))

graph = Graph(towns, adjacencies_path.read_text().split('\n'))

start_town = end_town = None

while start_town is None and end_town is None: # set starting/ending towns
    
    start_town = input('Please choose a starting town: ')
    end_town = input('Please choose a ending town: ')
    
    if start_town in towns and end_town in towns:
        
        start_town, end_town = towns[start_town], towns[end_town]
        print()

    elif start_town not in towns and end_town in towns:
        
        print(f'Start town {start_town} is not in database. Please try again.')
        
    elif end_town not in towns and start_town in towns:
        
        print(f'End town {end_town} is not in database. Please try again.')
        
    else:
        
        print(
            f'Neither {start_town} or {end_town} are in database. Please try again.')
    
while True: # main program
    
    user_input = input(
        'Choose from:\n1 - Breadth-first search\n2 - Depth-first search\n3 - ID-DFS search\n4 - Best-first search\n5 - A* search\n6 - Exit\n'
        )
    
    if user_input == '1': # Breadth-first search
    
        time = timeit.timeit(
            'graph.breadth_first_search(start_town)', globals=globals(), number=1000
            )
        print(f'Breadth-first search took {time} sec')

    elif user_input == '2': # Depth-first search
    
        time = timeit.timeit(
            'graph.depth_first_search(start_town, end_town)', globals=globals()
            )
        print(f'Depth-first search took {time} sec')

    elif user_input == '3': # ID-DFS search
    
        time = timeit.timeit(
            'graph.ID_DFS(start_town, end_town)', globals=globals()
            )
        print(f'ID-DFS search took {time} sec')

    elif user_input == '4': # Best-first search
    
        time = timeit.timeit(
            'graph.best_first_search(start_town, end_town)', globals=globals()
            )
        print(f'Best-first search took {time} sec')

    elif user_input == '5': # A* search
    
        time = timeit.timeit(
            'graph.astar(start_town, end_town)', globals=globals()
            )
        print(f'A* search took {time} sec')
        
    elif user_input == '6': # Exit
    
        break