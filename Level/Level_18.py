class Level_18:
    def __init__(self):
        pass

    def generate_level_18(self):
        self.level18 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟥", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟩", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "🟨", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟦", "🟨", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "🟥", "🟩", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "red", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "green", "white", "black", "white", "white"],
                ["black", "yellow", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "blue", "yellow", "black"],
                ["black", "white", "white", "black", "white", "white", "black", "red", "green", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "free", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟥", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "🟩", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "🟨", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "🟦", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "red", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "green", "white", "black", "white", "white"],
                ["black", "yellow", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "black", "white", "white", "black", "white", "blue", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level18

    def generate_goal_18(self):
        self.goal18 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "black", "white", "white"],
                ["black", "white", "white", "white", "black", "white", "white", "black", "white", "white"],
                ["black", "white", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "black", "white", "white", "black", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal18