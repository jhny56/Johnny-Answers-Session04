from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name:str, battery_level:int, status:str):
        """ INITIALIZING ROBOT (testing docstring ...)"""
        self.name = name
        self.battery_level = battery_level
        self.status = status

    def charge(self):
        self.battery_level = 100

    @abstractmethod
    def work(self):
        print("work mechanism start")

    def report_status(self):
        print("robot name : " + self.name)
        print("robot status : " + self.status)

    def decreasing_battery(self,amount:int):
        if(self.battery_level - amount <= 0):
            self.battery_level = 0
        else:
            self.battery_level = self.battery_level - amount
        return self.battery_level

    #get set name
    def get_name(self) -> str: 
        return self.name 
    def set_name(self, x:str): 
        self.name = x 

    #get set battery_level
    def get_battery_level(self) -> int: 
        return self.battery_level 
    def set_battery_level(self, x:int): 
        if(x < 0):
            self.battery_level = 0
        elif(x>100):
            self.battery_level = 100
        else:
            self.battery_level = x 

    #get set status
    def get_status(self) -> str: 
        return self.status 
    def set_status(self, x:str): 
        self.status = x 
