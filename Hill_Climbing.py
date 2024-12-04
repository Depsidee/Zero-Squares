import State
from collections import deque
class Hill_Climbing:
    def __init__(self):
        pass
    
    def play_Hill_Climbing(self, init_state, goal_state):
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
            for next_state in current_state.state_space():
                minimum = min(minimum, next_state.get_heuristic())
            for next_state in current_state.state_space():
                if next_state.get_heuristic() == minimum:
                    if minimum < current_state.get_heuristic():
                        parent[next_state] = current_state
                        new_state = next_state
                    else:
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
