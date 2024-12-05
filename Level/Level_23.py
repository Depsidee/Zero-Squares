class Level_23:
    def __init__(self):
        pass

    def generate_level_23(self):
        self.level23 = {
            "grid": [
                ["⬜️", "⬜️", "🔲", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬜️", "🔲", "⬜️", "🟦", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "🟥", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "🟦", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "color": [
                ["white", "white", "open_black", "black", "black", "black", "black"],
                ["white", "open_black", "white", "blue", "white", "white", "black"],
                ["open_black", "red", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "red", "white", "white", "black", "white", "black"],
                ["black", "blue", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "🔲", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬜️", "🔲", "⬜️", "🟦", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "fixed_color": [
                ["white", "white", "open_black", "black", "black", "black", "black"],
                ["white", "open_black", "white", "blue", "white", "white", "black"],
                ["open_black", "red", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level23

    def generate_goal_23(self):
        self.goal23 = {
            "grid": [
                ["⬜️", "⬜️", "🔲", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬜️", "🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "color": [
                ["white", "white", "open_black", "black", "black", "black", "black"],
                ["white", "open_black", "white", "white", "white", "white", "black"],
                ["open_black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal23
