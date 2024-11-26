import Levels
import State
import Move
import BFS
import DFS
import Recursive_DFS
import copy

class Main:
    levels = Levels.Levels()
    move = Move.Move()
    level_number = 1
    level, goal = levels.new_level(level_number)
    states = []
    pre_state = State.State(level["grid"],level["color"],level["status"])
    goal_state = State.State(goal["grid"],goal["color"],goal["status"])
    states.append(pre_state)
    print(pre_state.show())
    pre_state.state_space()
    
    continue_loop = True
    while continue_loop == True:
        x = input()
        
        """ Computer Plays """
        if x == "bfs":
            bfs = BFS.BFS()
            path = bfs.play_BFS(pre_state,goal_state)
        elif x == "dfs":
            dfs = DFS.DFS()
            path = dfs.play_DFS(pre_state,goal_state)
        elif x == "recursive dfs":
            recursive_dfs = Recursive_DFS.Recursive_DFS()
            path = recursive_dfs.play_recursive_DFS(pre_state,goal_state)
            
        level_number += 1
        level, goal = levels.new_level(level_number)
        if level == False:
            print("Congratulations, You have finished the game.")
            continue_loop = False
        else:
            pre_state = State.State(level["grid"],level["color"],level["status"])
            goal_state = State.State(goal["grid"],goal["color"],goal["status"])
         
        """ User Plays  """  
        """ if x == "right":
            next_state = move.move_right(pre_state)
        elif x == "left":
            next_state = move.move_left(pre_state)
        elif x == "up":
            next_state = move.move_up(pre_state)
        elif x == "down":
            next_state = move.move_down(pre_state)
            
        states.append(next_state)
        print(next_state.show())
        this_state_space = next_state.state_space()
        
        if next_state.check_win() == True:
            print("You Won.")
            level_number += 1
            level, goal = levels.new_level(level_number)
            if level == False:
                print("Congratulations, You have finished the game.")
                continue_loop = False
            else:
                pre_state = State.State(level["grid"],level["color"],level["status"])
                next_state = copy.deepcopy(pre_state)
        
        pre_state = copy.deepcopy(next_state)
        pre_state.stateSpace.clear() """
        

        