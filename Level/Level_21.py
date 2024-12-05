class Level_21:
    def __init__(self):
        pass

    def generate_level_21(self):
        self.level21 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟥", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "red", "white", "white", "white", "white", "white", "white", "white", "open_black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "red", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟥", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "open_black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "red", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level21

    def generate_goal_21(self):
        self.goal21 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]    
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "open_black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal21
