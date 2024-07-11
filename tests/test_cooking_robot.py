from ..src.robots.cooking_robot import CookingRobot

def testCookingRobot():

    testrobot = CookingRobot("testname",1000,"idle", "mal3a")

    print(testrobot.get_cooking_skill())

    testrobot.work()
    testrobot.report_status()
    testrobot.set_cooking_skill("chawke")
    testrobot.report_status()