class Controller:
    
    def __init__ (self, setpoint, Kp, read_fun):
        """! 
        Creates a Controller Object by initializing a setpoint (a desired location for the motor)
        a Kp value given by a user, and a encoder read function from an Encoder Object.

        @param setpoint This is a location for the motor in units of encoder counts.
        @param Kp A control gain set by the user. This is used to produce the actuation signal.
        @param read_fun This is a read function from an Encoder Object.
        """
        self.Kp=Kp
        self.setpoint=setpoint
        self.output_fun=read_fun
        
    def run(self,meas_output):
        """!
        This function runs the controller and changes the PWM for the next cycle.
    
        @param meas_output This value is the previous measured output.
        """
        self.PWM=self.Kp*(self.setpoint-self.meas_output)
    
    def set_setpoint(self,setpoint):
        """!
        This function sets the setpoint for the controller object.
    
        @param setpoint This is a location for the motor in units of encoder counts.
        """
        self.setpoint=setpoint
        
    def set_Kp(self,Kp):
        """!
        This function sets the Kp value for the controller object.
    
        @param Kp A control gain set by the user. This is used to produce the actuation signal.
        """
        self.Kp=Kp
        
    
    