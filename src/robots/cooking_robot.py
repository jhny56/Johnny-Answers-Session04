from .base_robot import Robot

class CookingRobot(Robot):
    def __init__(self, name:str, battery_level:int, status:str, cooking_skill:str):
        super().__init__(name,battery_level,status)
        self.cooking_skill = cooking_skill

    def work(self):
        print("Cooking mechanism start")
        print("Decreasing battery by 30%")
        Robot.decreasing_battery(self, 30)

    def self_diagnose(self):
        print("Cooking mechanism self diagnose start")


    #get set cooking_skill
    def get_cooking_skill(self) -> str: 
        return self.cooking_skill 
    def set_cooking_skill(self, x:str): 
        self.cooking_skill = x 
   