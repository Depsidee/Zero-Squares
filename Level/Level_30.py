class Level_30:
    def __init__(self):
        pass

    def generate_level_30(self):
        self.level30 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "🟪", "⬛️", "⬛️", "⬛️", "🟨", "⬛️", "⬛️", "🟩", "⬛️"],
                ["⬛️", "🟥", "🟦", "🟩", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "🟨", "🟪", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "🔳", "⬛️", "⬛️", "🟦", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "purple", "black", "black", "black", "yellow", "black", "black", "green", "black"],
                ["black", "red", "blue", "green", "white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "yellow", "purple", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "open_white", "black", "black", "blue", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "open_black", "black", "white", "white", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "🟪", "⬛️", "⬛️", "⬛️", "🟨", "⬛️", "⬛️", "🟩", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "🔳", "⬛️", "⬛️", "🟦", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "fixed_color": [
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "purple", "black", "black", "black", "yellow", "black", "black", "green", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "open_white", "black", "black", "blue", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "open_black", "black", "white", "white", "white", "white", "white", "white"]
            ]
        }
        return self.level30

    def generate_goal_30(self):
        self.goal30 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white", "black", "black", "black", "white", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "white", "black", "black", "white", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "open_black", "black", "white", "white", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal30
    
