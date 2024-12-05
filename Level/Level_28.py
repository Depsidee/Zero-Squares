class Level_28:
    def __init__(self):
        pass

    def generate_level_28(self):
        self.level28 = {
            "grid": [
                ["⬛️", "🔲", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "🔲", "⬛️"],
                ["⬛️", "🔳", "🟥", "⬜️", "⬜️", "🟦", "⬜️", "🟨", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟥", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "🟨", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "open_black", "black", "black", "black", "open_black", "black", "black", "open_black", "black"],
                ["black", "open_white", "red", "white", "white", "blue", "white", "yellow", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "red", "white", "black"],
                ["black", "black", "white", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "black", "black", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "yellow", "white", "open_black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "fixed", "fixed", "free", "fixed", "free", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
            ],
            "fixed_grid": [
                ["⬛️", "🔲", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "🔲", "⬛️"],
                ["⬛️", "🔳", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "🟥", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "🟨", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "fixed_color": [
                ["black", "open_black", "black", "black", "black", "open_black", "black", "black", "open_black", "black"],
                ["black", "open_white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "red", "white", "black"],
                ["black", "black", "white", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "black", "black", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "yellow", "white", "open_black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
            ]
        }
        return self.level28

    def generate_goal_28(self):
        self.goal28 = {
            "grid": [
                ["⬛️", "🔲", "⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "🔲", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "🔲"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],
            ],
            "color": [
                ["black", "open_black", "black", "black", "black", "open_black", "black", "black", "open_black", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "white", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "black", "black", "black", "black", "white", "black", "black", "white", "black"],
                ["white", "white", "white", "white", "black", "white", "white", "white", "white", "open_black"],
                ["white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
            ]
        }
        return self.goal28
