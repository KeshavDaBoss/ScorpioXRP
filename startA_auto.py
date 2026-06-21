from XRPLib.gamepad import *
from XRPLib.differential_drive import DifferentialDrive

gp = Gamepad.get_default_gamepad()

differentialDrive = DifferentialDrive.get_default_differential_drive()


while not (gp.is_button_pressed(gp.BUTTON_B)):
  if gp.is_button_pressed(gp.BUTTON_A):
    differentialDrive.turn((-90), 0.5)
    differentialDrive.straight(15, 0.8)
    differentialDrive.turn((-35), 0.5)
    differentialDrive.straight(15, 0.8)
    differentialDrive.turn(100, 0.5)
    differentialDrive.straight(15, 0.8)
    differentialDrive.turn(35, 0.5)
    differentialDrive.straight(82, 0.8)
    differentialDrive.turn((-15), 0.5)
    differentialDrive.straight((-100), 0.8)
    differentialDrive.turn((-90), 0.5)
    differentialDrive.straight(35, 0.8)
    differentialDrive.turn(90, 0.5)
    differentialDrive.straight(22, 0.8)
    differentialDrive.turn(40, 0.5)
    differentialDrive.straight(74, 0.8)
    differentialDrive.turn((-34), 0.5)
    differentialDrive.straight((-125), 0.8)