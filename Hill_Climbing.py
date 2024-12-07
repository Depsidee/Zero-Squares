import State
from collections import deque
import sys
class Hill_Climbing:
    sys.setrecursionlimit(100000)
    
    def __init__(self):
        pass
    
    def play_Simple_Hill_Climbing(self, init_state, goal_state):
         visited = set()
         parent = {}
         parent[init_state] = None
         
         current_state = init_state
         while current_state != None:
                if current_state in visited:
                    continue
                visited.add(current_state)
                
                if current_state.grid == goal_state.grid:
                    path = self.get_path(parent, current_state)
                    print(f"Number of visited states = {len(visited)}")
                    return path
                continue_algorithm = False
                new_state = current_state
                for next_state in current_state.state_space():
                    if next_state.get_heuristic() < current_state.get_heuristic():
                        parent[next_state] = current_state
                        new_state = next_state
                        continue_algorithm = True
                        break
                if continue_algorithm == False :
                    print("Algorithm has stopped.")
                    path = self.get_current_path(parent, current_state)
                    print(f"Number of visited states = {len(visited)}")
                    return path
                current_state = new_state
            
         return None
    
    def play_Steepest_Ascent_Hill_Climbing(self, init_state, goal_state):
         visited = set()
         parent = {}
         parent[init_state] = None
         
         minimum = 1000000000
         current_state = init_state
         while current_state != None:
                if current_state in visited:
                    continue
                visited.add(current_state)
                
                if current_state.grid == goal_state.grid:
                    path = self.get_path(parent, current_state)
                    print(f"Number of visited states = {len(visited)}")
                    return path
                new_state = current_state
                print(current_state.show())
                for next_state in current_state.state_space():
                    if next_state.get_heuristic() < minimum:
                        minimum = next_state.get_heuristic()
                        new_state = next_state
                if minimum < current_state.get_heuristic():
                    parent[new_state] = current_state
                else:
                    print("Algorithm has stopped.")
                    path = self.get_current_path(parent, current_state)
                    print(f"Number of visited states = {len(visited)}")
                    return path
                current_state = new_state
            
         return None
    
    def get_path(self, parent, goal_state):
        path = []
        current_state = goal_state
        while current_state is not None:
            path.append(current_state)
            current_state = parent[current_state]
        
        path.reverse()
        self.print_path(path)
        print(f"number of states in path = {len(path)}")
        return path
    
    def print_path(self, path):
        for state in path:
            print(state.show())
            print(f"heuristic = {state.get_heuristic()}")
            print()
    
    def get_current_path(self, parent, state):
        path = []
        current_state = state
        while current_state is not None:
            path.append(current_state)
            current_state = parent[current_state]
        
        path.reverse()
        self.print_path(path)
        print(f"number of states in path = {len(path)}")
        return path
