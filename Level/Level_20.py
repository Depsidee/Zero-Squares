class Level_20:
    def __init__(self):
        pass

    def generate_level_20(self):
        self.level20 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "🟥", "🟨", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟦", "🟪", "🟦", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "🟩", "⬛️", "🟥", "⬜️", "⬛️", "🟨", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "black", "white", "white"],
                ["black", "black", "black", "black", "red", "yellow", "black", "black", "black"],
                ["black", "blue", "purple", "blue", "white", "white", "white", "white", "black"],
                ["black", "white", "green", "black", "red", "white", "black", "yellow", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "🟨", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "🟦", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "🟪", "⬛️", "🟥", "⬜️", "⬛️", "🟩", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "fixed_color": [
                ["white", "white", "white", "black", "black", "black", "black", "white", "white"],
                ["black", "black", "black", "black", "white", "yellow", "black", "black", "black"],
                ["black", "blue", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "purple", "black", "red", "white", "black", "green", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ]
        }
        return self.level20

    def generate_goal_20(self):
        self.goal20 = {
            "grid": [
                ["⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "black", "white", "white"],
                ["black", "black", "black", "black", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "black", "white", "white", "black", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal20
