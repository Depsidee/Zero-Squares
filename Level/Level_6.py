class Level_6:
    def __init__(self):
        pass
    
    def generate_level_6(self):
        self.level6 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️"],
                ["⬛️","🟥","⬜️","⬜️","⬜️","⬛️","⬛️","⬜️","⬜️"],
                ["⬛️","⬜️","⬜️","🟦","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","🟦","🟥","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "red", "white", "white", "white", "black", "black", "white", "white"],
                ["black", "white", "white", "blue", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "blue", "red", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed","free", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️"],
                ["⬛️","🟥","⬜️","⬜️","⬜️","⬛️","⬛️","⬜️","⬜️"],
                ["⬛️","⬜️","⬜️","🟦","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "red", "white", "white", "white", "black", "black", "white", "white"],
                ["black", "white", "white", "blue", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "rwhite", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level6
    
    def generate_goal_6(self):
        self.goal6 = {
            "grid": [
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬜️","⬜️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "white", "white", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal6