import motor


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
    motor.dispense()
    input("Press Enter to continue...")
    motor.dispense()
    input("Press Enter to continue...")
    motor.reset_dispenser()
    input("Press Enter to continue...")
    return


def main():
    motor.init_motor(motor.MOTOR_RIGHT)
    motor.init_motor(motor.MOTOR_LEFT)
    motor.init_motor(motor.MOTOR_DISPENSER)

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