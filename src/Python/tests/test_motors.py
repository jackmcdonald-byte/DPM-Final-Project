from Python.main.motor import MotorController

MOTOR_CONTROLLER = MotorController()


def individual_motor_test():
    return


def forward_movement_test():
    motor.move_distance_forward(0.5, 100)
    return


def rotation_test():
    motor.rotate(90, 180)
    return


def dispenser_motor_test():
    input("Press Enter to continue...")
    MOTOR_CONTROLLER.dispense()
    input("Press Enter to continue...")
    MOTOR_CONTROLLER.dispense()
    input("Press Enter to continue...")
    MOTOR_CONTROLLER.reset_dispenser()
    input("Press Enter to continue...")
    return


def main():
    MOTOR_CONTROLLER.init_motor(motor.MOTOR_RIGHT)
    MOTOR_CONTROLLER.init_motor(motor.MOTOR_LEFT)
    MOTOR_CONTROLLER.init_motor(motor.MOTOR_DISPENSER)

    individual_motor_test()
    input("Press Enter to continue...")
    forward_movement_test()
    input("Press Enter to continue...")
    rotation_test()
    dispenser_motor_test()
    input("Press Enter to continue...")
    return

if __name__ == '__main__':
    main()