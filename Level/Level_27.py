class Level_27:
    def __init__(self):
        pass

    def generate_level_27(self):
        self.level27 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["🔲", "🔳", "🟦", "⬜️", "⬜️", "⬜️", "⬜️", "🟥", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "🟩", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "🟦", "🟩", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["open_black", "open_white", "blue", "white", "white", "white", "white", "red", "black", "white", "white"],
                ["black", "green", "white", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "blue", "green", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "black", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["🔲", "🔳", "🟦", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "🟩", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["open_black", "open_white", "blue", "white", "white", "white", "white", "white", "black", "white", "white"],
                ["black", "green", "white", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "black", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level27

    def generate_goal_27(self):
        self.goal27 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["open_black", "white", "white", "white", "white", "white", "white", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "black", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "white", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
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
        return self.goal27
