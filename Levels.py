from Level import Level_1
from Level import Level_2
from Level import Level_3
from Level import Level_4
from Level import Level_5
from Level import Level_6
from Level import Level_7
from Level import Level_8
from Level import Level_9
from Level import Level_10
from Level import Level_11
from Level import Level_12

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
        elif level_number == 4:
            level_4 = Level_4.Level_4()
            return level_4.generate_level_4(), level_4.generate_goal_4()
        elif level_number == 5:
            level_5 = Level_5.Level_5()
            return level_5.generate_level_5(), level_5.generate_goal_5()
        elif level_number == 6:
            level_6 = Level_6.Level_6()
            return level_6.generate_level_6(), level_6.generate_goal_6()
        elif level_number == 7:
            level_7 = Level_7.Level_7()
            return level_7.generate_level_7(), level_7.generate_goal_7()
        elif level_number == 8:
            level_8 = Level_8.Level_8()
            return level_8.generate_level_8(), level_8.generate_goal_8()
        elif level_number == 9:
            level_9 = Level_9.Level_9()
            return level_9.generate_level_9(), level_9.generate_goal_9()
        elif level_number == 10:
            level_10 = Level_10.Level_10()
            return level_10.generate_level_10(), level_10.generate_goal_10()
        elif level_number == 11:
            level_11 = Level_11.Level_11()
            return level_11.generate_level_11(), level_11.generate_goal_11()
        elif level_number == 12:
            level_12 = Level_12.Level_12()
            return level_12.generate_level_12(), level_12.generate_goal_12()
        else:
            return False, False