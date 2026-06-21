# Import Libraries
from XRPLib.board import Board
from XRPLib.gamepad import Gamepad
from XRPLib.differential_drive import DifferentialDrive
from XRPLib.servo import Servo
import time

# Initialize components
board = Board.get_default_board()
gp = Gamepad.get_default_gamepad()
differentialDrive = DifferentialDrive.get_default_differential_drive()
servo1 = Servo.get_default_servo(1)
servo2 = Servo.get_default_servo(2)
servo3 = Servo.get_default_servo(3)

# Constants
DEADBAND = 0.05
MODE_MANUAL = 0
MODE_AUTO_A = 1
MODE_AUTO_B = 2

current_mode = MODE_MANUAL

# Tank-Drive Function for Joystick to Motor Effort
def joystick_to_effort(value):
    if abs(value) < DEADBAND:
        return 0
    return max(-1, min(1, value))

# Helper function to check for Emergency Stop
def check_emergency_stop():
    if gp.is_button_pressed(gp.BUTTON_X):
        differentialDrive.set_effort(0, 0) # Kill motor power instantly
        return True
    return False

while True: # Mode Switching Logic
    if gp.is_button_pressed(gp.BUTTON_A):
        current_mode = MODE_AUTO_A
    elif gp.is_button_pressed(gp.BUTTON_B):
        current_mode = MODE_AUTO_B

    if current_mode == MODE_AUTO_A: # MODE AUTO A
    
        time.sleep(3.0)
        differentialDrive.turn(-15, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(100, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn(118, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(-30, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        time.sleep(0.3)
        servo1.set_angle(70)
        servo3.set_angle(130)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        time.sleep(0.3)
        servo2.set_angle(50)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        time.sleep(0.3)
        differentialDrive.straight(30, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn(-118, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(-100, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn(15, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn((-90), 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(10, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn((-35), 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(14, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn(100, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(10, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn(47, 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(85, 1)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.turn((-22), 0.5)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight((-130), 1)
        
        current_mode = MODE_MANUAL
        
    elif current_mode == MODE_AUTO_B: # MODE AUTO B
        differentialDrive.straight(-10, 0.8)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        time.sleep(0.3)
        servo1.set_angle(70)
        servo3.set_angle(130)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        time.sleep(0.3)
        servo2.set_angle(50)
        if check_emergency_stop(): current_mode = MODE_MANUAL; continue
        differentialDrive.straight(10, 0.8)
        current_mode = MODE_MANUAL

    else: # MANUAL MODE
        
        # Joystick Controls
        left_effort = joystick_to_effort(gp.get_value(gp.Y1))
        right_effort = joystick_to_effort(gp.get_value(gp.Y2))
        
        # D-Pad Controls
        if gp.is_button_pressed(gp.DPAD_UP): differentialDrive.straight(10, 1)
        if gp.is_button_pressed(gp.DPAD_DN): differentialDrive.straight(-10, 1)
        if gp.is_button_pressed(gp.DPAD_L): differentialDrive.turn(10, 0.5)
        if gp.is_button_pressed(gp.DPAD_R): differentialDrive.turn(-10, 0.5)
        
        # Servo Controls
        if gp.is_button_pressed(gp.TRIGGER_R):
            servo1.set_angle(70)
            servo3.set_angle(130)
        if gp.is_button_pressed(gp.TRIGGER_L):
            servo1.set_angle(0)
            servo3.set_angle(200)
        if gp.is_button_pressed(gp.BUMPER_R): servo2.set_angle(60)
        if gp.is_button_pressed(gp.BUMPER_L): servo2.set_angle(0)
        
        # 25x25x25 Mode
        if gp.is_button_pressed(gp.BUTTON_Y):
            servo1.set_angle(100)
            servo3.set_angle(100)

        differentialDrive.set_effort(0.8*left_effort, right_effort)
    
    time.sleep(0.02)