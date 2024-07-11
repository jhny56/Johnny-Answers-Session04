from tests.test_base_robot import testBaseRobot
from tests.test_cleaning_robot import testCleaningRobot
from tests.test_cooking_robot import testCookingRobot

from src.robots.maintenance_robot import MaintencanceRobot

def main():
    print("TESTING BASE ROBOT : ")
    # testBaseRobot()

    print("TESTING CLEANING ROBOT : ")
    testCleaningRobot()

    print("TESTING COOKING ROBOT : ")
    testCookingRobot()

    maintrobot = MaintencanceRobot("testname",1000,"idle", "Choffata","stool")
    maintrobot.multi_task()

main()

# from robots.cleaning_robot import CleaningRobot

# def testBaseRobot():
#     robottest = CleaningRobot("testname",1000,"idle", "Choffata")

#     print(robottest.get_name())
#     print(robottest.get_battery_level())
#     print(robottest.get_status())

#     robottest.set_battery_level(100)
#     assert robottest.decreasing_battery(10) == 90

#     robottest.report_status()
#     robottest.set_battery_level(-10)
#     robottest.set_name("testname 2")
#     robottest.set_status("Working")

#     robottest.report_status()

#     print(robottest.get_cleaning_tool())

#     robottest.work()
#     robottest.report_status()
#     robottest.set_cleaning_tool("messe7a")
#     robottest.report_status()

# testBaseRobot()