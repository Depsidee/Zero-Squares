class Level_25:
    def __init__(self):
        pass

    def generate_level_25(self):
        self.level25 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "🟥", "⬜️", "⬛️", "⬜️", "⬜️", "🟦", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["🔲", "⬜️", "⬜️", "🟥", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "🟨", "⬜️", "⬜️", "⬜️", "🟦", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "🟨", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "🔲", "⬛️", "⬛️"], 
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "red", "white", "black", "white", "white", "blue", "black", "white", "white", "white"],
                ["open_black", "white", "white", "red", "white", "white", "white", "open_black", "white", "white", "white"],
                ["black", "yellow", "white", "white", "white", "blue", "white", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "open_black", "white", "yellow", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "black", "open_black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["🔲", "⬜️", "⬜️", "🟥", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "🟨", "⬜️", "⬜️", "⬜️", "🟦", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "⬜️", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "🔲", "⬛️", "⬛️"], 
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "black", "white", "white", "white", "black", "white", "white", "white"],
                ["open_black", "white", "white", "red", "white", "white", "white", "open_black", "white", "white", "white"],
                ["black", "yellow", "white", "white", "white", "blue", "white", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "open_black", "white", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "black", "open_black", "black", "black"]
            ]
        }
        return self.level25

    def generate_goal_25(self):
        self.goal25 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"], 
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "⬜️", "⬜️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲", "⬜️", "⬜️", "⬛️"], 
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "🔲", "⬛️", "⬛️"], 
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "black", "white", "white", "white", "black", "white", "white", "white"],
                ["open_black", "white", "white", "white", "white", "white", "white", "open_black", "white", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "open_black", "white", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "white", "black", "open_black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal25
