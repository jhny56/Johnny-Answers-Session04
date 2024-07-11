from ..src.robots.base_robot import Robot

robottest = Robot("testname",1000,"idle")

print(robottest.get_name())
print(robottest.get_battery_level())
print(robottest.get_status())

robottest.decreasing_battery(10)
robottest.report_status()
robottest.set_battery_level(-10)
robottest.set_name("testname 2")
robottest.set_status("Working")

robottest.report_status()
