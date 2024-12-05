class Level_26:
    def __init__(self):
        pass

    def generate_level_26(self):
        self.level26 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "🟪", "⬛️"], 
                ["⬛️", "🔳", "🟩", "🟨", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "🟩", "🟪", "🟨", "🟥", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["white", "white", "white", "white", "white", "white", "white", "white", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "black", "black", "white", "purple", "black"],
                ["black", "open_white", "green", "yellow", "black", "black", "black", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "green", "purple", "yellow", "red", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "free", "free", "free", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "🟪", "⬛️"], 
                ["⬛️", "🔳", "🟩", "🟨", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "fixed_color": [
                ["white", "white", "white", "white", "white", "white", "white", "white", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "black", "black", "white", "purple", "black"],
                ["black", "open_white", "green", "yellow", "black", "black", "black", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level26

    def generate_goal_26(self):
        self.goal26 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"], 
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"], 
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["white", "white", "white", "white", "white", "white", "white", "white", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "black", "black", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal26
