"""!
@file nucleo_main.py

This file contains code that was stored on our group's Nucleo board to generate the motor step-response. 
This file was called by the code on our computer and read through the serial port to generate graphs of our step-response.
The file below imports the three different classes we had previoulsy set up to run the motor. 
The code below sets ups the motor, encoder, and controller classes necassary with their various pins. 
After initilization, the code then starts a loop where it asks for a Kp value and then runs the given Kp value in a motor step-response. 

@author Abe Muldrow
@author Lucas Rambo
@author Peter Tomson
"""

from controller import Controller
from motor_driver import MotorDriver
from encoder_reader import EncoderReader
import utime


motor1=MotorDriver('PC1','PA0','PA1',5)

encoder1=EncoderReader('PC6','PC7',8)

controller1=Controller(3300,1,encoder1)


while True:
    print('awaiting input')
    Kp=float(input('Input a Value for Kp: '))
    controller1.set_Kp(Kp)

    for i in range(300):
        utime.sleep_ms(10)
        controller1.input_obj.read()
        meas_output=controller1.input_obj.pos
        controller1.run(meas_output)
        PWM=controller1.PWM
        
        motor1.set_duty_cycle(PWM)
        
    controller1.input_obj.zero()
    motor1.set_duty_cycle(0)
    controller1.step_response()

        
        
