class State:
    def __init__(self, grid, color, status):
        self.grid = grid
        self.color = color
        self.status = status
    
    def show(self):
        str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                str += self.grid[i][j]
                str += " "
            str += "\n"
        return str
    
    def check_win(self):
        ans = True
        for i in range(len(self.status)):
            for j in range(len(self.status[i])):
                if self.status[i][j] == "free":
                    return False
        return ans