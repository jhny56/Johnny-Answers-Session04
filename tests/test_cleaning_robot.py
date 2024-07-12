import unittest
from src.robots.cleaning_robot import CleaningRobot
from test_base_robot import TestBaseRobot

class TestCleaningRobot(TestBaseRobot):

    def setUp(self):
        self.robot = CleaningRobot(name="CleanerBot", battery_level=100, status="Idle", cleaning_tool="Vacuum")

    def test_initialization(self):
        self.assertEqual(self.robot.get_cleaning_tool(), "Vacuum")

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 80)

    def test_self_diagnose(self):
        self.robot.self_diagnose()

    def test_set_cleaning_tool(self):
        self.robot.set_cleaning_tool("Brush")
        self.assertEqual(self.robot.get_cleaning_tool(), "Brush")

if __name__ == '__main__':
    unittest.main()
