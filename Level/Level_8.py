class Level_8:
    def __init__(self):
        pass
    
    def generate_level_8(self):
        self.level8 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","🟦","⬛️"],
                ["⬛️","⬜️","⬜️","🟦","⬛️","⬜️","⬛️"],
                ["⬛️","🟥","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟥","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "blue", "black"],
                ["black", "white", "white", "blue", "black", "white", "black"],
                ["black", "red", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "red", "black", "white", "black"],
                ["black", "white", "white", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","🟦","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟥","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "blue", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "red", "black", "white", "black"],
                ["black", "white", "white", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level8
    
    def generate_goal_8(self):
        self.goal8 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬛️","⬛️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
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
        return self.goal8