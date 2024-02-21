


class Controller:
    
    
    def __init__ (self, setpoint, Kp, read_fun):
        """! 
        Creates a encoder by initializing GPIO
        pins, setting up the correct timer channels, and creating the values
        needed to calculate the position change of the motor. 

        @param in1pin This is the value for the first pin name needed to set up the encoder. This value is input as a string of the pin name.
        @param in2pin This is the value for the second pin name needed to set up the encoder. This value is input as a string of the pin name.
        @param timer This is the value for the timer channel of the motor. Set as a integer. 
        """
        self.Kp=Kp
        self.setpoint=setpoint
        self.output_fun=read_fun
        
        print ("Creating a controller!yaay")
        
    def run(self,meas_output):
        
        self.PWM=self.Kp*(self.setpoint-self.meas_output)

        
    def set_setpoint(self,setpoint):
        self.setpoint=setpoint
        
    def set_Kp(self,Kp):
        self.Kp=Kp
        
    
    