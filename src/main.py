from tests.test_base_robot import testBaseRobot
from tests.test_cleaning_robot import testCleaningRobot
from tests.test_cooking_robot import testCookingRobot


def main():
    print("TESTING BASE ROBOT : ")
    testBaseRobot()

    print("TESTING CLEANING ROBOT : ")
    testCleaningRobot()

    print("TESTING COOKING ROBOT : ")
    testCookingRobot()


main()