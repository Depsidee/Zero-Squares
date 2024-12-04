class Level_12:
    def __init__(self):
        pass

    def generate_level_12(self):
        self.level12 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],  
                ["⬛️", "⬛️", "⬛️", "⬜️", "🟨", "⬜️", "⬛️"],  
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟥", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟨", "⬛️"],  
                ["⬛️", "⬛️", "🟦", "⬜️", "⬛️", "🟦", "⬛️"],  
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],  
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],  
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "white", "yellow", "white", "black"],
                ["black", "red", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "red", "black"],
                ["black", "white", "white", "white", "black", "yellow", "black"],
                ["black", "black", "blue", "white", "black", "blue", "black"],
                ["white", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "black", "black", "black", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],  
                ["⬛️", "⬛️", "⬛️", "⬜️", "🟨", "⬜️", "⬛️"],  
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬛️", "⬛️", "🟦", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],  
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],  
            ],
            "fixed_color": [
                ["white", "white", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "white", "yellow", "white", "black"],
                ["black", "red", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "blue", "white", "black", "white", "black"],
                ["white", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "black", "black", "black", "white", "white"]
            ]
        }
        return self.level12
    
    def generate_goal_12(self):
        self.goal12 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],  
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],  
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],  
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],  
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "white", "white", "black", "white", "black"],
                ["white", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "black", "black", "black", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal12

