class Level_15:
    def __init__(self):
        pass

    def generate_level_15(self):
        self.level15 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "🟦", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "🟨", "🟥", "🟦", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "🟨", "⬛️", "🟥", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "blue", "white", "black", "white", "black"],
                ["black", "black", "white", "black", "black", "black", "white", "black"],
                ["black", "white", "yellow", "red", "blue", "white", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "white", "yellow", "black", "red", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "free", "free", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "🟦", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "🟨", "⬛️", "🟥", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "fixed_color": [
                ["white", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "blue", "white", "black", "white", "black"],
                ["black", "black", "white", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "white", "yellow", "black", "red", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level15

    def generate_goal_15(self):
        self.goal15 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "black", "black"],
                ["white", "black", "white", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "white", "black", "black", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "black", "black", "black", "white", "black"],
                ["black", "white", "black", "white", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal15