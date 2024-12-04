import State
import heapq
class A_star:
    def __init__(self):
        pass
    
    def play_A_star(self, init_state, goal_state):
         visited = set()
         pq = []
         parent = {}
         cost = {}
         heuristic = {}
         parent[init_state] = None
         cost[init_state] = 0
         heuristic[init_state] = cost[init_state] + init_state.get_heuristic()
         heapq.heappush(pq, (heuristic[init_state], init_state))
         
         while len(pq) > 0:
            current_heuristic, current_state = heapq.heappop(pq)
            current_cost = cost[current_state]
            if current_state in visited:
                continue
            visited.add(current_state)
            
            if current_state.grid == goal_state.grid:
                path = self.get_path(parent, current_state)
                print(f"Number of visited states = {len(visited)}")
                return path
            for next_state in current_state.state_space():
                new_cost = current_cost + 1
                if next_state not in parent or (next_state in cost and new_cost < cost[next_state]):
                    parent[next_state] = current_state
                    cost[next_state] = new_cost
                    heuristic[next_state] = cost[next_state] + next_state.get_heuristic()
                    heapq.heappush(pq, (heuristic[next_state], next_state))
            
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
