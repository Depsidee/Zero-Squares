class Level_7:
    def __init__(self):
        pass
    
    def generate_level_7(self):
        self.level7 = {
            "grid": [
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","🟥","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","🟥","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟦","⬛️","🟦","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "red", "black", "white", "black"],
                ["black", "white", "white", "white", "red", "white", "black", "white", "black"],
                ["black", "white", "white", "blue", "black", "blue", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black","black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed","fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]  
            ],
            "fixed_grid": [
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","🟥","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟦","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "fixed_color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "red", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "blue", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black","black"]
            ]
        }
        return self.level7
    
    def generate_goal_7(self):
        self.goal7 = {
            "grid": [
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ],
            "color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black","black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed","fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]  
            ]
        }
        return self.goal7