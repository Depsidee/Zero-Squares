class Level_17:
    def __init__(self):
        pass

    def generate_level_17(self):
        self.level17 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "🟦", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "🟨", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "🟩", "⬜️", "🟩", "⬛️", "🟥", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "🟨", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "🟦", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"]   
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "red", "white", "white", "white", "blue", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "yellow", "black"],
                ["black", "black", "black", "black", "white", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "white", "white", "black"],
                ["black", "green", "white", "green", "black", "red", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "yellow", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "blue", "black"],
                ["white", "white", "white", "white", "white", "white", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "free", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "🟨", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "🟩", "⬛️", "🟥", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "🟦", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"]   
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "yellow", "black"],
                ["black", "black", "black", "black", "white", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "green", "black", "red", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "blue", "black"],
                ["white", "white", "white", "white", "white", "white", "black", "black", "black"]
            ]
        }
        return self.level17

    def generate_goal_17(self):
        self.goal17 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬛️"],
                ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️"]   
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "white", "white"],
                ["black", "white", "white", "white", "white", "white", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "black"],
                ["black", "black", "black", "black", "white", "white", "black", "white", "black"],
                ["white", "white", "black", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "white", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "black", "black", "black", "black", "black", "black", "white", "black"],
                ["white", "white", "white", "white", "white", "white", "black", "black", "black"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal17