class Level_10:
    def __init__(self):
        pass

    def generate_level_10(self):
        self.level10 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "🟦", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "🟥", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟦", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "black", "black", "white", "white", "white", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "white", "white", "black", "white", "blue", "black", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "white", "red", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "black", "black", "white", "black"],
                ["black", "red", "black", "white", "black", "black", "white", "white", "white", "black", "blue", "black"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black","black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "🟦", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "fixed_color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "black", "black", "white", "white", "white", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "white", "white", "black", "white", "blue", "black", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "white", "red", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "black", "black", "white", "black"],
                ["black", "white", "black", "white", "black", "black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black","black", "black", "black"]
            ]
        }
        return self.level10
    
    def generate_goal_10(self):
        self.goal10 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "black", "black", "white", "white", "white", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "white", "white", "black", "white", "white", "black", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "black", "black", "white", "black"],
                ["black", "white", "black", "white", "black", "black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black","black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal10

