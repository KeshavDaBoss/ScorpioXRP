from XRPLib.board import Board
from XRPLib.gamepad import Gamepad
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.servo import Servo

import time


board = Board.get_default_board()
gamepad = Gamepad.get_default_gamepad()
drive = DifferentialDrive.get_default_differential_drive()
servo1 = Servo.get_default_servo(1)
servo3 = Servo.get_default_servo(3)
servo2 = Servo.get_default_servo(2)

DEADBAND = 0.05


def joystick_to_effort(value):
    if abs(value) < DEADBAND:
        return 0

    if value > 1:
        return 1

    if value < -1:
        return -1

    return value


try:
    while not board.is_button_pressed():
        left_effort = joystick_to_effort(gamepad.get_value(Gamepad.Y1))
        right_effort = joystick_to_effort(gamepad.get_value(Gamepad.Y2))
        
        if gamepad.is_button_pressed(Gamepad.DPAD_UP):
           drive.straight(5, 0.5)
        if gamepad.is_button_pressed(Gamepad.DPAD_DN):
           drive.straight((-5), 0.5)   
        if gamepad.is_button_pressed(Gamepad.DPAD_L):
           drive.turn((20), 0.5)
        if gamepad.is_button_pressed(Gamepad.DPAD_R):
           drive.turn(-20, 0.5)

        
        if gamepad.is_button_pressed(gamepad.TRIGGER_R):
           servo1.set_angle(30)
           servo3.set_angle(170)
        if gamepad.is_button_pressed(gamepad.TRIGGER_L):
           servo1.set_angle(0)
           servo3.set_angle(200)
        if gamepad.is_button_pressed(gamepad.BUMPER_R):
           servo2.set_angle(50)
        if gamepad.is_button_pressed(gamepad.BUMPER_L):
           servo2.set_angle(0)

        drive.set_effort(left_effort, right_effort)
        time.sleep(0.02)
finally:
    drive.stop()