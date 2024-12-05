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
from Level import Level_13
from Level import Level_14
from Level import Level_15
from Level import Level_16
from Level import Level_17
from Level import Level_18
from Level import Level_19
from Level import Level_20
from Level import Level_21
from Level import Level_22
from Level import Level_23
from Level import Level_24
from Level import Level_25

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
        elif level_number == 13:
            level_13 = Level_13.Level_13()
            return level_13.generate_level_13(), level_13.generate_goal_13()
        elif level_number == 14:
            level_14 = Level_14.Level_14()
            return level_14.generate_level_14(), level_14.generate_goal_14()
        elif level_number == 15:
            level_15 = Level_15.Level_15()
            return level_15.generate_level_15(), level_15.generate_goal_15()
        elif level_number == 16:
            level_16 = Level_16.Level_16()
            return level_16.generate_level_16(), level_16.generate_goal_16()
        elif level_number == 17:
            level_17 = Level_17.Level_17()
            return level_17.generate_level_17(), level_17.generate_goal_17()
        elif level_number == 18:
            level_18 = Level_18.Level_18()
            return level_18.generate_level_18(), level_18.generate_goal_18()
        elif level_number == 19:
            level_19 = Level_19.Level_19()
            return level_19.generate_level_19(), level_19.generate_goal_19()
        elif level_number == 20:
            level_20 = Level_20.Level_20()
            return level_20.generate_level_20(), level_20.generate_goal_20()
        elif level_number == 21:
            level_21 = Level_21.Level_21()
            return level_21.generate_level_21(), level_21.generate_goal_21()
        elif level_number == 22:
            level_22 = Level_22.Level_22()
            return level_22.generate_level_22(), level_22.generate_goal_22()
        elif level_number == 23:
            level_23 = Level_23.Level_23()
            return level_23.generate_level_23(), level_23.generate_goal_23()
        elif level_number == 24:
            level_24 = Level_24.Level_24()
            return level_24.generate_level_24(), level_24.generate_goal_24()
        elif level_number == 25:
            level_25 = Level_25.Level_25()
            return level_25.generate_level_25(), level_25.generate_goal_25()
        else:
            return False, False