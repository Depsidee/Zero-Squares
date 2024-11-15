import Level_1
import Level_2
import Level_3

import copy

class Levels:
    def __init__(self) -> None:
        pass
          
    def new_level(self, level_number):
        if level_number == 1:
            level_1 = Level_1.Level_1()
            return level_1.generate_level_1(), level_1.generate_goal_1()
        elif level_number == 2:
            level_2 = Level_2.Level_2()
            return level_2.generate_level_2(), level_2.generate_goal_2()
        elif level_number == 3:
            level_3 = Level_3.Level_3()
            return level_3.generate_level_3(), level_3.generate_goal_3()
        else:
            return False, False