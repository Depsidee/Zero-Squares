class Level_11:
    def __init__(self):
        pass

    def generate_level_11(self):
        self.level11 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],   
                ["⬛️", "⬛️", "🟨", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "🟨", "🟥", "🟦", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["⬛️", "🟦", "⬛️", "🟥", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],   
            ],
            "color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "yellow", "black", "black", "black", "black", "black"],
                ["black", "yellow", "red", "blue", "white", "white", "white", "black"],
                ["black", "blue", "black", "red", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "free", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],   
                ["⬛️", "⬛️", "🟨", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["⬛️", "🟦", "⬛️", "🟥", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],   
            ],
            "fixed_color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "yellow", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "blue", "black", "red", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white"]
            ]
        }
        return self.level11
    
    def generate_goal_11(self):
        self.goal11 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],   
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],   
            ],
            "color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "white", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal11

