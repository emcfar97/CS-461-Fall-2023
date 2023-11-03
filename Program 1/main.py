import csv, pathlib, timeit, heapq
from collections import defaultdict, deque
from queue import PriorityQueue
from math import dist

class Graph:
    'This class represents a directed graph using adjacency list representation'
 
    def __init__(self, nodes, vertices):
        'Constructor'
 
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        
        # Populate graph
        for vertice in vertices:
            
            town_a, town_b = vertice.split()
            
            self.graph[nodes[town_a]].append(nodes[town_b])
      
    def breadth_first_search(self, root, target, display=1):
        'Function to print a BFS of graph'
  
        # Create queues for visited and unvisited nodes
        visited, queue = set(), deque([root])
        visited.add(root)
 
        while queue:
 
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            if display: print(str(vertex) + " ")

            # If not visited, mark it as visited, and enqueue it
            for neighbor in self.graph[vertex]:
                
                if target == neighbor: 
                    
                    if display: print(neighbor)
                    return
                
                elif neighbor not in visited:
                    
                    visited.add(neighbor)
                    queue.append(neighbor)
        
    def DFSUtil(self, root, target, visited, display):
        'Function used by DFS'
 
        # Mark the current node as visited and print it
        visited.add(root)
        if display: print(root)
 
        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[root]:
            
            if root == neighbor:
                
                if display: print(neighbor)
                return
                
            if neighbor not in visited:
                
                self.DFSUtil(neighbor, target, visited, display)
 
    def depth_first_search(self, root, target, display=1):
        'Function to do DFS traversal. It uses recursive DFSUtil()'
 
        # Create a set to store visited vertices
        visited = set()
 
        # Call the recursive helper function to print DFS traversal
        self.DFSUtil(root, target, visited, display)
 
    def DLS(self, root, target, maxDepth, display):
        'Function to perform a Depth-Limited search from given source "root"'
 
        if root == target: return True
 
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False
 
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[root]:

            if display: print(i)
                
            if (self.DLS(i, target, maxDepth-1, display)):

                return True

        return False
 
    def ID_DFS(self, root, target, maxDepth=3, display=1):
        'ID-DFS to search if target is reachable from v'

        if display: print(root)
        
        # Repeatedly depth-limit search till the maximum depth
        for i in range(1, maxDepth):
            
            if display: print(f'\nAt depth {i}:')
            
            if (self.DLS(root, target, i, display)):
                
                return True
            
        return False
    
    def best_first_search(self, root, target, display=1):
        'Function to print a BFS of graph'

        visited = set()
        examined = PriorityQueue()
        examined.put((0, root))
        visited.add(root)
        
        while examined.empty() == False:

            u = examined.get()[1]
            
            # Displaying the path having lowest cost
            if display: print(u)

            if u == target: break
    
            for vertice in self.graph[u]:
                
                cost = vertice % u

                if vertice not in visited:

                    visited.add(vertice)
                    examined.put((cost, vertice))
    
    def heuristic(self, node, goal):
        
        x1, y1 = node.position
        x2, y2 = goal.position
        
        return abs(x1 - x2) + abs(y1 - y2)
    
    def get_neighbors(self, node):
        
        x, y = node.position
        neighbors = []
        
        for neighbor in self.graph[node]:
            
            if neighbor == node: continue 
            
            neighbors.append((neighbor, node, node % neighbor))

        return neighbors

    def astar(self, root, target, display=1):
        'Returns a list of tuples as a path from the given root to the given target'

        open_list = []
        closed_list = set()

        heapq.heappush(open_list, (0, root))
        
        while open_list:
            
            current_cost, current_node = heapq.heappop(open_list)

            # target reached, construct and return the path
            if current_node == target:
                
                path = []
                
                while current_node:
                    
                    path.append(current_node.position)
                    current_node = current_node[1]
                    
                return path[::-1]

            closed_list.add(current_node)

            for neighbor in self.get_neighbors(current_node):
                
                if neighbor in closed_list: continue

                if display: print(neighbor[0])
                
                new_cost = current_node % neighbor[0]
                
                if neighbor[0] not in open_list:
                    
                    heapq.heappush(
                        open_list, (new_cost + self.heuristic(neighbor[0], target), neighbor[0])
                        )
                    
                elif new_cost < neighbor[2]:
                    
                    neighbor[2] = new_cost
                    neighbor[1] = current_node

class Town():
    'Town class for Graph'
    
    def __init__(self, name, position):
        
        self.name = name
        self.position = position
        self.vistited = False
    
    def __repr__(self): return f'{self.name} {self.position}'
    
    def __add__(self, other):
        
        return (
            self.position[0] + other.position[0],
            self.position[1] + other.position[1]
            )
    
    def __sub__(self, other):
        
        return (
            self.position[0] - other.position[0],
            self.position[1] - other.position[1]
            )
    
    def __mod__(self, other): return dist(self.position, other.position)
    
    def set_visited(self): self.visited = not self.visited
    
    def get_visited(self): return self.visited
    
class Node():
    'Node class for A* Pathfinding'

    def __init__(self, position, parent=None, cost=0):
        
        self.position = position
        self.parent = parent
        self.cost = cost

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

while True: # set starting/ending towns
    
    start_town = input('Please choose a starting town: ')
    end_town = input('Please choose a ending town: ')
    
    if start_town in towns and end_town in towns:
        
        start_town, end_town = towns[start_town], towns[end_town]
        print()
        break

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
        
        graph.breadth_first_search(start_town, end_town)
        
        time = timeit.timeit(
            'graph.breadth_first_search(start_town, end_town, 0)', globals=globals(), number=100000
            )
        print(f'\nBreadth-first search took {time} sec\n')

    elif user_input == '2': # Depth-first search
    
        graph.depth_first_search(start_town, end_town)
        
        time = timeit.timeit(
            'graph.depth_first_search(start_town, end_town, 0)', globals=globals(), number=100000
            )
        print(f'\nDepth-first search took {time} sec\n')

    elif user_input == '3': # ID-DFS search
        
        try:
            
            maxDepth = int(input('Enter maxDepth (default=3): ') or '3')
            
        except:
            
            print('Input is not a number')
            continue
            
        if graph.ID_DFS(start_town, end_town, maxDepth) == True:

            print ("Target is reachable from source within max depth")

        else:

            print ("Target is NOT reachable from source within max depth")
    
        time = timeit.timeit(
            f'graph.ID_DFS(start_town, end_town, {maxDepth}, display=0)', globals=globals(), number=100000
            )
        print(f'\nID-DFS search took {time} sec\n')

    elif user_input == '4': # Best-first search
                
        graph.best_first_search(start_town, end_town)
        
        time = timeit.timeit(
            'graph.best_first_search(start_town, end_town, 0)', globals=globals(), number=100000
            )
        print(f'\nBest-first search took {time} sec\n')

    elif user_input == '5': # A* search
        
        graph.astar(start_town, end_town)
        
        time = timeit.timeit(
            'graph.astar(start_town, end_town, 0)', globals=globals(), number=100000
            )
        print(f'\nA* search took {time} sec\n')
        
    elif user_input == '6': # Exit
    
        break