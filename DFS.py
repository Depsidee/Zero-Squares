import State
from collections import deque
import sys
class DFS:
    sys.setrecursionlimit(100000)
    
    def __init__(self):
        pass
    
    def play_DFS(self, init_state, goal_state):
         visited = set()
         s = []
         parent = {}
         s.append(init_state)
         parent[init_state] = None
         
         while len(s) > 0:
            current_state = s.pop()
            if current_state in visited:
                continue
            visited.add(current_state)
            
            if current_state.grid == goal_state.grid:
                path = self.get_path(parent, current_state)
                print(f"Number of visited states = {len(visited)}")
                return path
            """ print(current_state.show())
            print(len(current_state.state_space())) """
            for next_state in current_state.state_space():
                if next_state not in visited:
                    parent[next_state] = current_state
                    s.append(next_state)
            
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
