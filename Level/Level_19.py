class Level_19:
    def __init__(self):
        pass

    def generate_level_19(self):
        self.level19 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "🟨", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟦", "⬜️", "⬜️", "🟨", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "🟥", "⬜️", "⬛️", "🟥", "⬜️", "🟩", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟦", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "🟩", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️"],
            ],
            "color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "yellow", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white"],
                ["black", "black", "black", "white", "black", "black", "black", "black"],
                ["black", "blue", "white", "white", "yellow", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "red", "white", "black", "red", "white", "green", "black"],
                ["black", "black", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "white", "black", "white", "blue", "white", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "black"],
                ["white", "white", "white", "black", "black", "green", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "🟨", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "🟥", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "🟦", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "🟩", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️"],
            ],
            "fixed_color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "yellow", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white"],
                ["black", "black", "black", "white", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "black", "red", "white", "white", "black"],
                ["black", "black", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "white", "black", "white", "blue", "white", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "black"],
                ["white", "white", "white", "black", "black", "green", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "white"]
            ]
        }
        return self.level19

    def generate_goal_19(self):
        self.goal19 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️"],
            ],
            "color": [
                ["white", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "white", "black", "black", "white", "white", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "white"],
                ["black", "black", "black", "white", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "white", "black", "black", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "black"],
                ["white", "white", "white", "black", "white", "white", "white", "black"],
                ["white", "white", "white", "black", "black", "white", "black", "black"],
                ["white", "white", "white", "white", "black", "black", "black", "white"]
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
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal19