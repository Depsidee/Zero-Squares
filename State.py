import Move

move = Move.Move()

class State:
    def __init__(self, grid, color, status):
        self.grid = grid
        self.color = color
        self.status = status
        self.stateSpace = []
    
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return (self.grid == other.grid and
            self.color == other.color and
            self.status == other.status)
        
    
    def __hash__(self):
         return hash((tuple(map(tuple, self.grid)), 
                     tuple(map(tuple, self.color)), 
                     tuple(map(tuple, self.status))))
    
    def state_space(self):
        next_state = move.move_right(self)
        if self.grid != next_state.grid :
            self.stateSpace.append(next_state)
        
        next_state = move.move_left(self)
        if self.grid != next_state.grid :
            self.stateSpace.append(next_state)
        
        next_state = move.move_up(self)
        if self.grid != next_state.grid :
            self.stateSpace.append(next_state)
        
        next_state = move.move_down(self)
        if self.grid != next_state.grid :
            self.stateSpace.append(next_state)
        
        """ if len(self.stateSpace) != 0 :
            print("State Space for this state:")
            print(self.print_state_space()) """
        
        return self.stateSpace
    
    def show(self):
        str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                str += self.grid[i][j]
                #str += " "
            str += "\n"
        return str
    
    def print_state_space(self):
        str = ""
        for i in range(len(self.grid)):
            for state in self.stateSpace:
                    for j in range(len(state.grid[i])):
                        str += state.grid[i][j]
                        #str += " "
                    str += "  "
            str += "\n"
        return str
    
    def check_win(self):
        ans = True
        for i in range(len(self.status)):
            for j in range(len(self.status[i])):
                if self.status[i][j] == "free":
                    return False
        return ans