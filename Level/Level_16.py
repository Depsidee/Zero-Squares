class Level_16:
    def __init__(self):
        pass

    def generate_level_16(self):
        self.level16 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟨", "🟥", "🟦", "🟩", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟨", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "🟩", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "🟦", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "yellow", "red", "blue", "green", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "yellow", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "green", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "blue", "white", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "red", "white", "white", "black", "white", "white", "white", "white"],
                ["white", "black", "black", "black", "black", "black", "black", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "free", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟨", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "🟩", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "🟦", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "🟥", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "yellow", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "green", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "blue", "white", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "red", "white", "white", "black", "white", "white", "white", "white"],
                ["white", "black", "black", "black", "black", "black", "black", "white", "white", "white", "white"]
            ]
        }
        return self.level16

    def generate_goal_16(self):
        self.goal16 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "white", "white", "white", "black", "white", "white", "white", "white"],
                ["white", "black", "black", "black", "black", "black", "black", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal16
