import Controller
import MotorDriver
import EncoderReader
import utime


motor1=MotorDriver('PC1','PA0','PA1',5)

encoder1=EncoderReader('PC6','PC7',8)

controller1=Controller(10000,100,encoder1.read())

meas_output=controller1.run()
print(meas_output)
    
    
    
    