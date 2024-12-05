class Level_13:
    def __init__(self):
        pass

    def generate_level_13(self):
        self.level13 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬛️", "⬛️", "🟦", "🟥", "🟨", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🟦", "⬛️","⬛️", "⬛️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️","⬛️", "🟥","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️","⬛️", "⬜️","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️","⬜️", "⬜️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬛️", "🟨", "⬜️", "⬜️","⬜️", "⬛️","⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬛️", "⬛️","⬜️", "⬜️"],    
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "black", "blue", "red", "yellow", "black", "white", "white", "white", "white"],
                ["black", "white", "black", "white", "white", "blue", "black", "black", "black", "black", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "red", "white", "black"],
                ["black", "white", "black", "black", "white", "black", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "yellow", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"]
            ],
            "status": [
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "free", "free", "free", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"],
                ["fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed", "fixed"]
            ],
            "fixed_grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "🟦", "⬛️","⬛️", "⬛️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️","⬛️", "🟥","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️","⬛️", "⬜️","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️","⬜️", "⬜️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬛️", "🟨", "⬜️", "⬜️","⬜️", "⬛️","⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬛️", "⬛️","⬜️", "⬜️"],    
            ],
            "fixed_color": [
                ["white", "white", "black", "black", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "black", "white", "white", "white", "black", "white", "white", "white", "white"],
                ["black", "white", "black", "white", "white", "blue", "black", "black", "black", "black", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "red", "white", "black"],
                ["black", "white", "black", "black", "white", "black", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "yellow", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"]
            ]
        }
        return self.level13
    
    def generate_goal_13(self):
        self.goal13 = {
            "grid": [
                ["⬜️", "⬜️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬛️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️","⬜️", "⬜️","⬜️", "⬜️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬛️","⬛️", "⬛️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️", "⬜️","⬛️", "⬜️","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬛️", "⬛️", "⬜️", "⬛️", "⬛️","⬛️", "⬜️","⬜️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️","⬜️", "⬜️","⬛️", "⬛️"],  
                ["⬛️", "⬜️", "⬜️", "⬛️", "⬜️", "⬜️", "⬜️","⬜️", "⬛️","⬛️", "⬜️"],
                ["⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️", "⬛️","⬛️", "⬛️","⬜️", "⬜️"],    
            ],
            "color": [
                ["white", "white", "black", "black", "black", "black", "black", "white", "white", "white", "white"],
                ["black", "black", "black", "white", "white", "white", "black", "white", "white", "white", "white"],
                ["black", "white", "black", "white", "white", "white", "black", "black", "black", "black", "black"],
                ["black", "white", "black", "white", "white", "white", "white", "black", "white", "white", "black"],
                ["black", "white", "black", "black", "white", "black", "black", "black", "white", "white", "black"],
                ["black", "white", "white", "white", "white", "white", "white", "white", "white", "black", "black"],
                ["black", "white", "white", "black", "white", "white", "white", "white", "black", "black", "white"],
                ["black", "black", "black", "black", "black", "black", "black", "black", "black", "white", "white"]
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
        return self.goal13

