class Level_29:
    def __init__(self):
        pass

    def generate_level_29(self):
        self.level29 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "🟥", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "🟨", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "🟪", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "🟦", "🟦", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "🔳", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟨", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "white", "white", "white", "black", "black", "white", "red", "white", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white", "yellow", "white", "white", "black"],
                ["black", "purple", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "blue", "blue", "black", "white", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "black", "black", "black", "white", "open_white", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "yellow", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "red", "white", "white", "white", "white", "white", "open_black"],
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "🟦", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "🔳", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟨", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "fixed_color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "white", "white", "white", "black", "black", "white", "white", "white", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "blue", "black", "white", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "black", "black", "black", "white", "open_white", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "yellow", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "red", "white", "white", "white", "white", "white", "open_black"],
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level29

    def generate_goal_29(self):
        self.goal29 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["white", "white", "white", "white", "black", "black", "white", "white", "white", "black", "black", "black"],
                ["black", "black", "black", "black", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "black", "white", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "black", "black", "black", "white", "white", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "open_black"],
                ["white", "white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
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
        return self.goal29
