from ..src.robots.cleaning_robot import CleaningRobot

def testCleaningRobot():

    testrobot = CleaningRobot("testname",1000,"idle", "Choffata")

    print(testrobot.get_cleaning_tool())

    testrobot.work()
    testrobot.report_status()
    testrobot.set_cleaning_tool("messe7a")
    testrobot.report_status()

testCleaningRobot()