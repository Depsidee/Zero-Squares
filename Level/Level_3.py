class Level_3:
    def __init__(self):
        pass
    
    def generate_level_3(self):
        self.level3 = {
            "grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬛️","🟥","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","🟥","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "color": [
                ["white","white","black","black","black","black","black","black","black","black","black","black","black"],
                ["white","white","black","red","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","white","white","black","black","black","black","black","black","white","black"],
                ["black","white","white","white","white","white","red","white","white","white","black","white","black"],
                ["black","white","black","white","white","white","white","white","white","white","black","white","black"],
                ["black","white","white","white","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","black","white","white","white","white","white","white","white","white","black"],
                ["white","white","white","black","black","black","black","black","black","black","black","black","black"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","free","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
            ],
            "fixed_grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","🟥","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "fixed_color": [
                ["white","white","black","black","black","black","black","black","black","black","black","black","black"],
                ["white","white","black","white","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","white","white","black","black","black","black","black","black","white","black"],
                ["black","white","white","white","white","white","red","white","white","white","black","white","black"],
                ["black","white","black","white","white","white","white","white","white","white","black","white","black"],
                ["black","white","white","white","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","black","white","white","white","white","white","white","white","white","black"],
                ["white","white","white","black","black","black","black","black","black","black","black","black","black"]
            ]
        }
        return self.level3
    
    def generate_goal_3(self):
        self.goal3 = {
            "grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "color": [
                ["white","white","black","black","black","black","black","black","black","black","black","black","black"],
                ["white","white","black","white","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","white","white","black","black","black","black","black","black","white","black"],
                ["black","white","white","white","white","white","white","white","white","white","black","white","black"],
                ["black","white","black","white","white","white","white","white","white","white","black","white","black"],
                ["black","white","white","white","white","white","white","white","white","white","white","white","black"],
                ["black","black","black","black","white","white","white","white","white","white","white","white","black"],
                ["white","white","white","black","black","black","black","black","black","black","black","black","black"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
            ]
        }
        return self.goal3