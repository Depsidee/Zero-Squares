import Move
import sys
move = Move.Move()

class State:
    sys.setrecursionlimit(100000)
    
    def __init__(self, grid, color, status, fixed_grid=[], fixed_color=[]):
        self.grid = grid
        self.color = color
        self.status = status
        self.fixed_grid = fixed_grid
        self.fixed_color = fixed_color
        self.stateSpace = []
        self.cost = 0
    
    def __eq__(self, other):
        if not isinstance(other, State):
            return False
        return (self.grid == other.grid and
            self.color == other.color and
            self.status == other.status)
        
    
    def __hash__(self):
         return hash((tuple(map(tuple, self.grid)), 
                     tuple(map(tuple, self.color)), 
                     tuple(map(tuple, self.status)),
                     tuple(map(tuple, self.fixed_grid)),
                     tuple(map(tuple, self.fixed_color))))
         
    def __lt__(self, other):
        return self.grid < other.grid
    
    def state_space(self):
        self.stateSpace.clear()
        
        if self.check_possibility():
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
                if self.status[i][j] == "free" or (self.color[i][j] not in ["white", "black", "open_black"]):
                    return False
        return ans
    
    def get_heuristic(self):
        heuristic = 0
        free = 0
        for i in range(len(self.status)):
            for j in range(len(self.status[i])):
                if self.status[i][j] == "free":
                    free += 1
                    for ii in range(len(self.fixed_grid)):
                        for jj in range(len(self.fixed_grid[ii])):
                            if sum(item.count(self.color[i][j]) for item in self.fixed_color) == 0:
                                if self.fixed_color[ii][jj] == "open_white":
                                   manhattan_dist = abs(i-ii)+abs(j-jj)
                                   heuristic += manhattan_dist
                            else:
                                if self.fixed_color[ii][jj] == self.color[i][j]:
                                    manhattan_dist = abs(i-ii)+abs(j-jj)
                                    heuristic += manhattan_dist
                                
        """ heuristic += free """
        return heuristic
    
    def check_possibility(self):
    
        if sum(item.count("red") for item in self.fixed_color) > 1:
            return False
        if sum(item.count("blue") for item in self.fixed_color) > 1:
            return False
        if sum(item.count("yellow") for item in self.fixed_color) > 1:
            return False
        if sum(item.count("green") for item in self.fixed_color) > 1:
            return False
        if sum(item.count("purple") for item in self.fixed_color) > 1:
            return False
        
        free = 0
        fixed = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.status[i][j] == "free":
                    free += 1
                if self.fixed_color[i][j] not in ["white", "black", "open_black"]:
                    fixed += 1
        if fixed != free:
            return False
        
        return True