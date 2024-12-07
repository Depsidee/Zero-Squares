class Level_4:
    def __init__(self):
        pass
    
    def generate_level_4(self):
        self.level4 = {
            "grid": [
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟥","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","🟥","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["white", "white", "white", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "red", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "red", "white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "free", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","🟥","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"]
            ],
            "fixed_color": [
                ["white", "white", "white", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["white", "white", "white", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "red", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"]
            ]
        }
        return self.level4
    
    def generate_goal_4(self):
        self.goal4 = {
            "grid": [
                ["⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬜️","⬜️","⬜️","⬛️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
                ["⬛️","⬜️","⬜️","⬜️","⬜️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"],
                ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬜️","⬜️","⬜️","⬜️","⬜️"]
            ],
            "color": [
                ["white", "white", "white", "black", "black", "black", "white", "white", "white", "white", "white"],
                ["white", "white", "white", "black", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "black", "black", "black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "white", "white", "black", "white", "white", "white", "white", "white"],
                ["black", "black", "black", "black", "black", "black", "white", "white", "white", "white", "white"]

            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
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
        return self.goal4