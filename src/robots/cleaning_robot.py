from .base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name:str, battery_level:int, status:str, cleaning_tool:str):
        super().__init__(name,battery_level,status)
        self.cleaning_tool = cleaning_tool

    def work(self):
        print("Cleaning mechanism start")
        print("Decreasing battery by 20%")
        Robot.decreasing_battery(self, 20)

    def self_diagnose(self):
        print("Cleaning mechanism self diagnose start")

    #get set cleaning_tool
    def get_cleaning_tool(self) ->str: 
        return self.cleaning_tool 
    def set_cleaning_tool(self, x:str): 
        self.cleaning_tool = x 

   

