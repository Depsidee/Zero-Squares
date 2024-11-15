import copy

class Level_1:
    def __init__(self):
        pass
    
    def generate_level_1(self):
        self.level1 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","💖","⬜️","⬜️","⬜️","⬜️","💖","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black","black","black","black","black","black","black","black"],
                ["black","red","white","white","white","white","red","black"],
                ["black","black","black","black","black","black","black","black"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","free","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"]
            ]
        }
        return self.level1
    
    def generate_goal_1(self):
        self.goal1 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black","black","black","black","black","black","black","black"],
                ["black","white","white","white","white","white","white","black"],
                ["black","black","black","black","black","black","black","black"]
            ],
            "status": [
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"],
                ["fixed","fixed","fixed","fixed","fixed","fixed","fixed","fixed"]
            ]
        }
        return self.goal1