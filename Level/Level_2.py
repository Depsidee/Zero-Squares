class Level_2:
    def __init__(self):
        pass
    
    def generate_level_2(self):
        self.level2 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","🟥","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","🟥","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "color": [
                ["black","black","black","black","black","black","black","black"],
                ["black","white","white","black","white","white","white","black"],
                ["black","red","white","white","white","white","white","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","black","black","black","red","black","black","black"],
                ["white","white","white","black","black","black","white","white"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","free","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"]
            ],
            "fixed_grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","🟥","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "fixed_color": [
                ["black","black","black","black","black","black","black","black"],
                ["black","white","white","black","white","white","white","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","black","black","black","red","black","black","black"],
                ["white","white","white","black","black","black","white","white"]
            ]
        }
        return self.level2
    
    def generate_goal_2(self):
        self.goal2 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "color": [
                ["black","black","black","black","black","black","black","black"],
                ["black","white","white","black","white","white","white","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","black","black","black","white","black","black","black"],
                ["white","white","white","black","black","black","white","white"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"]
            ]
        }
        return self.goal2