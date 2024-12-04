class Level_5:
    def __init__(self):
        pass
    
    def generate_level_5(self):
        self.level5 = {
            "grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
                ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
                ["⬜️","⬛️","⬛️","⬜️","⬜️","🟥","⬜️","⬜️","⬛️","⬜️"],
                ["⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","🟥","⬛️","⬜️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black", "white"],
                ["white", "black", "black", "white", "white", "red", "white", "white", "black", "white"],
                ["black", "black", "white", "white", "white", "white", "black", "red", "black", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "black","black"],
                ["black", "black", "black", "black", "black", "black","black", "black", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed","free", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
                ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
                ["⬜️","⬛️","⬛️","⬜️","⬜️","🟥","⬜️","⬜️","⬛️","⬜️"],
                ["⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "fixed_color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black", "white"],
                ["white", "black", "black", "white", "white", "red", "white", "white", "black", "white"],
                ["black", "black", "white", "white", "white", "white", "black", "white", "black", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "black","black"],
                ["black", "black", "black", "black", "black", "black","black", "black", "white", "white"]
            ]
        }
        return self.level5
    
    def generate_goal_5(self):
        self.goal5 = {
            "grid": [
                ["⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️"],
                ["⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
                ["⬜️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️"],
                ["⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬜️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️"]
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black", "white"],
                ["white", "black", "black", "white", "white", "white", "white", "white", "black", "white"],
                ["black", "black", "white", "white", "white", "white", "black", "white", "black", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "black","black"],
                ["black", "black", "black", "black", "black", "black","black", "black", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed","fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal5