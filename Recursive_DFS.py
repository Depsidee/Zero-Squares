class Recursive_DFS:
    def __init__(self):
        pass

    def play_recursive_DFS(self, current_state, goal_state, visited=None, parent=None):
        if visited is None:
            visited = set()
        if parent is None:
            parent = {}

        visited.add(current_state)

        if current_state.grid == goal_state.grid:
            return

        for next_state in current_state.state_space():
            if next_state not in visited:
                parent[next_state] = current_state
                result = self.play_recursive_DFS(next_state, goal_state, visited, parent)
                if result is not None: 
                    return result

        return None  
