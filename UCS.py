import State
import heapq
import sys

class UCS:
    sys.setrecursionlimit(100000)
    
    def __init__(self):
        pass
    
    def play_UCS(self, init_state, goal_state):
         visited = set()
         pq = []
         parent = {}
         cost = {}
         parent[init_state] = None
         cost[init_state] = init_state.cost
         heapq.heappush(pq, (cost[init_state], init_state))
         
         while len(pq) > 0:
            current_cost, current_state = heapq.heappop(pq)
            if current_state in visited:
                continue
            visited.add(current_state)
            
            if current_state.grid == goal_state.grid:
                path = self.get_path(parent, current_state, cost)
                print(f"Number of visited states = {len(visited)}")
                return path
            """ print(current_state.show())
            print(len(current_state.state_space())) """
            for next_state in current_state.state_space():
                new_cost = current_cost + next_state.cost
                if next_state not in parent or (next_state in cost and new_cost < cost[next_state]):
                    parent[next_state] = current_state
                    cost[next_state] = new_cost
                    heapq.heappush(pq, (new_cost, next_state))
            
         return None
    
    def get_path(self, parent, goal_state, cost):
        path = []
        current_state = goal_state
        while current_state is not None:
            path.append(current_state)
            current_state = parent[current_state]
        
        path.reverse()
        self.print_path(path, cost)
        print(f"number of states in path = {len(path)}")
        return path
    
    def print_path(self, path, cost):
        for state in path:
            print(state.show())
            print(f"cost = {cost[state]}")
