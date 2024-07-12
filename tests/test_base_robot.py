import unittest
from src.robots.base_robot import Robot

class TestableRobot(Robot):
    def work(self):
        pass

    def self_diagnose(self):
        print("TestableRobot self diagnose")

class TestBaseRobot(unittest.TestCase):

    def setUp(self):
        self.robot = TestableRobot(name="BaseBot", battery_level=100, status="Idle")

    def test_initialization(self):
        self.assertEqual(self.robot.get_name(), "BaseBot")
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.assertEqual(self.robot.get_status(), "Idle")

    def test_charge(self):
        self.robot.charge()
        self.assertEqual(self.robot.get_battery_level(), 100)

    def test_decreasing_battery(self):
        self.robot.decreasing_battery(30)
        self.assertEqual(self.robot.get_battery_level(), 70)

    def test_decreasing_battery_to_zero(self):
        self.robot.decreasing_battery(110)
        self.assertEqual(self.robot.get_battery_level(), 0)

    def test_set_name(self):
        self.robot.set_name("BaseBotV2")
        self.assertEqual(self.robot.get_name(), "BaseBotV2")

    def test_set_battery_level(self):
        self.robot.set_battery_level(50)
        self.assertEqual(self.robot.get_battery_level(), 50)
        self.robot.set_battery_level(150)
        self.assertEqual(self.robot.get_battery_level(), 100)
        self.robot.set_battery_level(-10)
        self.assertEqual(self.robot.get_battery_level(), 0)

    def test_set_status(self):
        self.robot.set_status("Working")
        self.assertEqual(self.robot.get_status(), "Working")
