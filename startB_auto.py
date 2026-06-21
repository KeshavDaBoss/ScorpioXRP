from XRPLib.gamepad import *
from XRPLib.differential_drive import DifferentialDrive

gp = Gamepad.get_default_gamepad()


differentialDrive = DifferentialDrive.get_default_differential_drive()


while not (gp.is_button_pressed(gp.BUTTON_X)):
  if gp.is_button_pressed(gp.BUTTON_B):
    differentialDrive.turn((-90), 0.5)
    differentialDrive.straight(10, 0.8)
    differentialDrive.turn(50, 0.5)
    differentialDrive.straight(20, 0.8)
    differentialDrive.turn((-50), 0.5)
    differentialDrive.straight(40, 0.8)
    differentialDrive.turn((-90), 0.5)
    differentialDrive.straight(30, 0.8)
    differentialDrive.turn((-90), 0.5)