from robot import Robot


def main():
    robot = Robot()
    robot.chassis.MotorController.stop()
    robot.run()


if __name__ == '__main__':
    main()