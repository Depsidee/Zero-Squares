import State
import sys
class Recursive_DFS:
    sys.setrecursionlimit(100000)
    
    def __init__(self):
        self.visited = set()
        self.parent = {}
        self.result = []
    
    def play_recursive_DFS(self, current_state, goal_state):
         
         if len(self.parent) == 0:
            self.parent[current_state] = None
         
         if current_state in self.visited:
            return self.result
         self.visited.add(current_state)
        
         if current_state.grid == goal_state.grid:
            path = self.get_path(self.parent, goal_state)
            print(f"Number of visited states = {len(self.visited)}")
            return path
         """ print(current_state.show())
         print(len(current_state.state_space())) """
         for next_state in current_state.state_space():
            if next_state not in self.visited:
                self.parent[next_state] = current_state
                self.result.append(self.play_recursive_DFS(next_state, goal_state))
            
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
