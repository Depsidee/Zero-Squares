import Levels
import State
import Move
import copy

class Main:
    levels = Levels.Levels()
    level_number = 1
    level = levels.new_level(level_number)
    states = []
    pre_state = State.State(level["grid"],level["color"],level["status"])
    states.append(pre_state)
    
    print(pre_state.show())
    move = Move.Move()
    continue_loop = True
    while continue_loop == True:
        x = input()
        if x == "right":
            next_state = move.move_right(pre_state)
        elif x == "left":
            next_state = move.move_left(pre_state)
        elif x == "up":
            next_state = move.move_up(pre_state)
        elif x == "down":
            next_state = move.move_down(pre_state)
        states.append(next_state)
        print(next_state.show())
        if next_state.check_win() == True:
            print("You Won.")
            level_number += 1
            level = levels.new_level(level_number)
            if level == False:
                print("Congratulations, You have finished the game.")
                continue_loop = False
            else:
                pre_state = State.State(level["grid"],level["color"],level["status"])
                next_state = copy.deepcopy(pre_state)
        pre_state = copy.deepcopy(next_state)
        

        