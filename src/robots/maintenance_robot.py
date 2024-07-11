from cooking_robot import CookingRobot
from cleaning_robot import CleaningRobot

class MaintencanceRobot(CookingRobot,CleaningRobot):
    def __init__(self, name:str, battery_level:int, status:str, cooking_skill:str,cleaning_tool:str):
        super(CookingRobot).__init__(name,battery_level,status,cooking_skill)
        self.cleaning_tool = cleaning_tool

    def multi_task(self):
        super(CookingRobot,self).work()
        super(CleaningRobot,self).work()


    #get set cooking_skill
    def get_cooking_skill(self) -> str: 
        return self.cooking_skill 
    def set_cooking_skill(self, x:str): 
        self.cooking_skill = x 
   