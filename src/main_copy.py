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
        #print(meas_output)
        
        
        controller1.run(meas_output)
        PWM=controller1.PWM
        
        motor1.set_duty_cycle(PWM)
        
    controller1.input_obj.zero()
    motor1.set_duty_cycle(0)
    controller1.step_response()

        
        
