class Level_22:
    def __init__(self):
        pass

    def generate_level_22(self):
        self.level22 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["🔲", "⬜️", "⬜️", "🟦", "⬜️", "⬜️", "🟥", "⬛️"],   
                ["⬛️", "⬜️", "🟦", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],   
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "⬛️", "⬜️"],  
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "black"],
                ["open_black", "white", "white", "blue", "white", "white", "red", "black"],
                ["black", "white", "blue", "white", "white", "white", "black", "black"],
                ["black", "red", "white", "white", "white", "white", "black", "white"],
                ["black", "black", "black", "open_black", "black", "black", "black", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "free", "fixed", "fixed", "free", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["⬛️", "⬜️", "🟦", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],   
                ["⬛️", "🟥", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "⬛️", "⬜️"],  
            ],
            "fixed_color": [
                ["black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "black"],
                ["open_black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "blue", "white", "white", "white", "black", "black"],
                ["black", "red", "white", "white", "white", "white", "black", "white"],
                ["black", "black", "black", "open_black", "black", "black", "black", "white"]
            ]
        }
        return self.level22

    def generate_goal_22(self):
        self.goal22 = {
            "grid": [
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["🔲", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬛️"],   
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "🔲", "⬛️", "⬛️", "⬛️", "⬜️"],  
            ],
            "color": [
                ["black", "black", "black", "black", "black", "black", "black", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "black"],
                ["open_black", "white", "white", "white", "white", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "white", "white", "white", "black", "white"],
                ["black", "black", "black", "open_black", "black", "black", "black", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ]
        }
        return self.goal22
