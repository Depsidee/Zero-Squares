class Level_9:
    def __init__(self):
        pass

    def generate_level_9(self):
        self.level9 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "🟥", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "🟦", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "🟥", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "🟦", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "red", "white", "white", "black", "black", "black", "black", "black", "white"],
                ["black", "white", "white", "white", "white", "black", "black", "blue", "white", "black", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "black", "black", "black", "white", "white", "red", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "blue", "white", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "black", "black", "black", "black", "white", "white", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "🟦", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "🟥", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "fixed_color": [
                ["white", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "white", "white", "white", "black", "black", "black", "black", "black", "white"],
                ["black", "white", "white", "white", "white", "black", "black", "blue", "white", "black", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "black", "black", "black", "white", "white", "red", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "white", "white", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "black", "black", "black", "black", "white", "white", "white", "white", "white", "white"]
            ]

        }
        return self.level9
    
    def generate_goal_9(self):
        self.goal9 = {
            "grid": [
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],
                ["⬛️", "⬛️", "⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️"],
                ["⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"]
            ],
            "color": [
                ["white", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "white", "white", "white", "black", "black", "black", "black", "black", "white"],
                ["black", "white", "white", "white", "white", "black", "black", "white", "white", "black", "white"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "black", "black", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "black", "white", "white", "black", "black", "black", "black", "black", "black", "white"],
                ["white", "black", "black", "black", "black", "white", "white", "white", "white", "white", "white"]
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
        return self.goal9

