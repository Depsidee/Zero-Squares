class Level_14:
    def __init__(self):
        pass

    def generate_level_14(self):
        self.level14 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟨", "⬛️", "🟥", "⬛️", "🟦", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "yellow", "black", "red", "black", "blue", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "free", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟦", "⬛️", "🟨", "⬛️", "🟥", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "blue", "black", "yellow", "black", "red", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level14

    def generate_goal_14(self):
        self.goal14 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "black", "white", "black", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "white", "white", "white", "white", "black"],
                ["white", "black", "black", "black", "black", "black", "black"]
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
        return self.goal14