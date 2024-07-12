import unittest
from src.robots.cooking_robot import CookingRobot
from test_base_robot import TestBaseRobot

class TestCookingRobot(TestBaseRobot):

    def setUp(self):
        self.robot = CookingRobot(name="CookerBot", battery_level=100, status="Idle", cooking_skill="Expert")

    def test_initialization(self):
        super().test_initialization()
        self.assertEqual(self.robot.get_cooking_skill(), "Expert")

    def test_work(self):
        self.robot.work()
        self.assertEqual(self.robot.get_battery_level(), 70)

    def test_self_diagnose(self):
        self.robot.self_diagnose()

    def test_set_cooking_skill(self):
        self.robot.set_cooking_skill("Intermediate")
        self.assertEqual(self.robot.get_cooking_skill(), "Intermediate")

if __name__ == '__main__':
    unittest.main()
