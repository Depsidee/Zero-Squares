class Level_24:
    def __init__(self):
        pass

    def generate_level_24(self):
        self.level24 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"], 
                ["⬛️", "⬛️", "🟨", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"], 
                ["🔲", "🟥", "⬜️", "🟨", "⬜️", "🟦", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "🟦", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["black", "black", "yellow", "white", "white", "white", "white", "white", "black", "black"],
                ["open_black", "red", "white", "yellow", "white", "blue", "white", "white", "white", "black"],
                ["open_black", "white", "white", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "red", "white", "white", "white", "white", "blue", "black", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "free", "fixed", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"], 
                ["⬛️", "⬛️", "🟨", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"], 
                ["🔲", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟦", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "fixed_color": [
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["black", "black", "yellow", "white", "white", "white", "white", "white", "black", "black"],
                ["open_black", "red", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["open_black", "white", "white", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "blue", "black", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level24

    def generate_goal_24(self):
        self.goal24 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"], 
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"], 
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["🔲", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"], 
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"], 
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "white"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["open_black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["open_black", "white", "white", "black", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal24
