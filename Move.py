import copy

class Move:
    def __init__(self):
        pass
    
    def move_right(self, pre_state):
        next_state = copy.deepcopy(pre_state)
        for i in range(len(pre_state.grid)):
            for j in range(len(pre_state.grid[i])-1,-1,-1):
                if pre_state.status[i][j] == "free":
                    next_state.grid[i][j] = "⬜️"
                    next_state.color[i][j] = "white"
                    next_state.status[i][j] = "fixed"
                    end, y = self.check_right(pre_state, next_state, i, j)
                    if end == True:
                        next_state.grid[i][y] = "⬜️"
                        next_state.color[i][y] = "white"
                        next_state.fixed_grid[i][y] = "⬜️"
                        next_state.fixed_color[i][y] = "white"
                    elif y != -1:
                        next_state.grid[i][y] = pre_state.grid[i][j]
                        next_state.color[i][y] = pre_state.color[i][j]
                        next_state.status[i][y] = pre_state.status[i][j]
        for i in range(len(next_state.grid)):
            for j in range(len(next_state.grid[i])):
                if next_state.grid[i][j] == "⬜️" and next_state.fixed_grid[i][j] != "⬜️":
                        next_state.grid[i][j] = next_state.fixed_grid[i][j]
                        next_state.color[i][j] = next_state.fixed_color[i][j]
        return next_state
    
    def move_left(self, pre_state):
        next_state = copy.deepcopy(pre_state)
        for i in range(len(pre_state.grid)):
            for j in range(len(pre_state.grid[i])):
                if pre_state.status[i][j] == "free":
                    next_state.grid[i][j] = "⬜️"
                    next_state.color[i][j] = "white"
                    next_state.status[i][j] = "fixed"
                    end, y = self.check_left(pre_state, next_state, i, j)
                    if end == True:
                        next_state.grid[i][y] = "⬜️"
                        next_state.color[i][y] = "white"
                        next_state.fixed_grid[i][y] = "⬜️"
                        next_state.fixed_color[i][y] = "white"
                    elif y != -1:
                        next_state.grid[i][y] = pre_state.grid[i][j]
                        next_state.color[i][y] = pre_state.color[i][j]
                        next_state.status[i][y] = pre_state.status[i][j]
        for i in range(len(next_state.grid)):
            for j in range(len(next_state.grid[i])):
                if next_state.grid[i][j] == "⬜️" and next_state.fixed_grid[i][j] != "⬜️":
                        next_state.grid[i][j] = next_state.fixed_grid[i][j]
                        next_state.color[i][j] = next_state.fixed_color[i][j]
        return next_state
    
    def move_up(self, pre_state):
        next_state = copy.deepcopy(pre_state)
        for i in range(len(pre_state.grid)):
            for j in range(len(pre_state.grid[i])):
                if pre_state.status[i][j] == "free":
                    next_state.grid[i][j] = "⬜️"
                    next_state.color[i][j] = "white"
                    next_state.status[i][j] = "fixed"
                    end, x = self.check_up(pre_state, next_state, i, j)
                    if end == True:
                        next_state.grid[x][j] = "⬜️"
                        next_state.color[x][j] = "white"
                        next_state.fixed_grid[x][j] = "⬜️"
                        next_state.fixed_color[x][j] = "white"
                    elif x != -1:
                        next_state.grid[x][j] = pre_state.grid[i][j]
                        next_state.color[x][j] = pre_state.color[i][j]
                        next_state.status[x][j] = pre_state.status[i][j]
        for i in range(len(next_state.grid)):
            for j in range(len(next_state.grid[i])):
                if next_state.grid[i][j] == "⬜️" and next_state.fixed_grid[i][j] != "⬜️":
                        next_state.grid[i][j] = next_state.fixed_grid[i][j]
                        next_state.color[i][j] = next_state.fixed_color[i][j]
        return next_state
    
    def move_down(self, pre_state):
        next_state = copy.deepcopy(pre_state)
        for i in range(len(pre_state.grid)-1,-1,-1):
            for j in range(len(pre_state.grid[i])):
                if pre_state.status[i][j] == "free":
                    next_state.grid[i][j] = "⬜️"
                    next_state.color[i][j] = "white"
                    next_state.status[i][j] = "fixed"
                    end, x = self.check_down(pre_state, next_state, i, j)
                    if end == True:
                        next_state.grid[x][j] = "⬜️"
                        next_state.color[x][j] = "white"
                        next_state.fixed_grid[x][j] = "⬜️"
                        next_state.fixed_color[x][j] = "white"
                    elif x != -1:
                        next_state.grid[x][j] = pre_state.grid[i][j]
                        next_state.color[x][j] = pre_state.color[i][j]
                        next_state.status[x][j] = pre_state.status[i][j]
        for i in range(len(next_state.grid)):
            for j in range(len(next_state.grid[i])):
                if next_state.grid[i][j] == "⬜️" and next_state.fixed_grid[i][j] != "⬜️":
                        next_state.grid[i][j] = next_state.fixed_grid[i][j]
                        next_state.color[i][j] = next_state.fixed_color[i][j]
        return next_state
    
    def check_right(self, pre_state, next_state, x, y):
        end = False
        j = y
        if y < len(pre_state.grid[x])-1 and pre_state.status[x][y+1] == "free":
            return end, j
        while end == False and j < len(pre_state.grid[x])-1:
            if next_state.status[x][j+1] == "free" or next_state.color[x][j+1] == "black":
                break
            if pre_state.color[x][j+1] == pre_state.color[x][y]:
                end = True
                j +=1
                break
            if next_state.color[x][j+1] == "open_black":
                return False, -1
            j += 1
        return end, j
    
    def check_left(self, pre_state, next_state, x, y):
        end = False
        j = y
        if y > 0 and pre_state.status[x][y-1] == "free":
            return end, j
        while end == False and j > 0:
            if next_state.status[x][j-1] == "free" or next_state.color[x][j-1] == "black":
                break
            if pre_state.color[x][j-1] == pre_state.color[x][y]:
                end = True
                j -=1
                break
            if next_state.color[x][j-1] == "open_black":
                return False, -1
            j -= 1
        return end, j
    
    def check_up(self, pre_state, next_state, x, y):
        end = False
        i = x
        if x > 0 and pre_state.status[x-1][y] == "free":
            return end, i
        while end == False and i > 0:
            if next_state.status[i-1][y] == "free" or next_state.color[i-1][y] == "black":
                break
            if pre_state.color[i-1][y] == pre_state.color[x][y]:
                end = True
                i -=1
                break
            if next_state.color[i-1][y] == "open_black":
                return False, -1
            i -= 1
        return end, i
    
    def check_down(self, pre_state, next_state, x, y):
        end = False
        i = x
        if x < len(pre_state.grid)-1 and pre_state.status[x+1][y] == "free":
            return end, i
        while end == False and i < len(pre_state.grid)-1:
            if next_state.status[i+1][y] == "free" or next_state.color[i+1][y] == "black":
                break
            if pre_state.color[i+1][y] == pre_state.color[x][y]:
                end = True
                i +=1
                break
            if next_state.color[i+1][y] == "open_black":
                return False, -1
            i += 1
        return end, i