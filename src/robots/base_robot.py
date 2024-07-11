from abc import ABC, abstractmethod

class Robot(ABC):
    def __init__(self, name, battery_level, status):
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

    def decreasing_battery(self,amount):
        if(self.battery_level - amount <= 0):
            self.battery_level = 0
        else:
            self.battery_level = self.battery_level - 20

