from base_robot import Robot

class CleaningRobot(Robot):
    def __init__(self, name, battery_level, status, cleaning_tool):
        super().__init__(name,battery_level,status)
        self.cleaning_tool = cleaning_tool

    def work(self):
        print("Cleaning mechanism start")
        print("Decreasing battery by 20%")
        Robot.decreasing_battery(self, 20)


   

