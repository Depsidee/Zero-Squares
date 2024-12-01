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
         parent[init_state] = None
         cost[init_state] = init_state.get_heuristic()
         heapq.heappush(pq, (cost[init_state], init_state))
         
         while len(pq) > 0:
            current_cost, current_state = heapq.heappop(pq)
            if current_state in visited:
                continue
            visited.add(current_state)
            
            if current_state.grid == goal_state.grid:
                path = self.get_path(parent, goal_state)
                print(f"Number of visited states = {len(visited)}")
                return path
            for next_state in current_state.state_space():
                new_cost = next_state.get_heuristic()
                if next_state not in parent or (next_state in cost and new_cost < cost[next_state]):
                    parent[next_state] = current_state
                    cost[next_state] = new_cost
                    heapq.heappush(pq, (new_cost, next_state))
            
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
