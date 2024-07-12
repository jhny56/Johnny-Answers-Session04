from src.robots.maintenance_robot import MaintencanceRobot
from src.robots.cleaning_robot import CleaningRobot
from src.robots.cooking_robot import CookingRobot



def main():
    

    maintrobot = MaintencanceRobot("Maintencance Robot 1",100,"idle", "Choffata","stool")
    maintrobot.report_status()
    while(maintrobot.get_battery_level > 0):
        maintrobot.multi_task()
        print(maintrobot.get_battery_level())
    
    maintrobot.charge()
    maintrobot.report_status()

main()

