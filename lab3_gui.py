"""!
@file lab0week2_final.py
This file contains code to run program on a laptop or desktop which creates a user interface
that can send a signal to the microcontroller to run a step response.
The code then takes the results of the step response from the microcontroller and plots it in the user interface.
Included in the GUI plot as well is a plot of a simulated V_max(1-e^-t/RC) curve. The
V_max, R, and C values are from are circuit and are 3.03 V, 100K Ohms, and 3.3 microF respectively.

The code used in main.py for our microcontroller can be found in the lab_00b.py file in our Doxygen and GitHub documentation. 

This file is uses code from lab0example.py file on on Cantvas and an example found at:
https://matplotlib.org/stable/gallery/user_interfaces/embedding_in_tk_sgskip.html

@author Abe Muldrow, Lucas Rambo, Peter Tomson
@date January 28th, 2024, Original program, based on example from above listed sources
"""

# imports 
import math
import time
import tkinter
import serial
from random import random
from serial import Serial
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


def step_reponse(plot_axes, plot_canvas, xlabel, ylabel):
    """!
    This function retrieves the data from the microcontroller to create the plot of the step response.
    The function first sens ASCII digits to the controller to stop any running program, get the controller into
    regular REPL mode, and then reboot the code to cause the main.py code on the board to run. The main.py file
    contains the code to generate the step response which is then read by this function through the serial port. 
    
    @param plot_axes The plot axes supplied by Matplotlib
    @param plot_canvas The plot canvas, also supplied by Matplotlib
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    """
    # set the serial port for reading from the microcontroller
    ser = serial.Serial("COM4", 9600)
    
    # reset and send commands to the board in ASCII
    # print("sending to board")
    print("waiting for data")
    ser.write(bytearray('\x03','ascii')) # ascii code for ctrl+c
    ser.write(bytearray('\x02','ascii')) # ctrl+b
    ser.write(bytearray('\x04','ascii')) # ctrl+d
    
    # create our variables for printing 
    array =[]	# create an array to store the data
    cont = 1	# variable for running the read function
    time=[]	 	# list to store our time values
    pos=[]	# list to store our volt values
    start=0 #boolean to show start of step response data
    # while cont is true read values from the serial port
    while cont == 1:
        value = ser.readline().decode('utf-8').strip()
        if value == 'start'
            start=1
            while start==1:
                value = ser.readline().decode('utf-8').strip()
            
                if value == 'end':	# once end is printed by the microcontroller stop reading values
                    
                    start = 0
                    cont=0
                else:
                    array.append(value)	# append values to out array
    for i in array:	# once we have retrieved the values from the board they must be added to our lists
        index = i.split(',')	# split x and y values
        try:  
            timeval  =float(index[0].strip('('))	# float and strip the value
            posval = float(index[1].strip(')'))
            time.append(timeval)	# add to out lists
            pos.append(posval)
        except:
            pass
   
    print('plotting data')
    
    # Draw the plot use plot_axes. Data labels, a legend, and axis tick marks are included.
    plot_axes.clear()	# clear the axes so there is no repeat legend
    plot_axes.plot(t, volts, label = 'Measured Response Data', color = 'deepskyblue', marker = '.' )
    plot_axes.set_xlabel(xlabel)
    plot_axes.set_ylabel(ylabel)
    plot_axes.grid(True)
    plot_axes.legend()
    plot_axes.axis([0, 2000, 0, 4000])
    plot_canvas.draw()


def tk_matplot(plot_function, xlabel, ylabel, title):
    """!
    The following function is from the lab0example code:
    
    Create a TK window with one embedded Matplotlib plot.
    This function makes the window, displays it, and runs the user interface
    until the user closes the window. The plot function, which must have been
    supplied by the user, should draw the plot on the supplied plot axes and
    call the draw() function belonging to the plot canvas to show the plot. 
    @param plot_function The function which, when run, creates a plot
    @param xlabel The label for the plot's horizontal axis
    @param ylabel The label for the plot's vertical axis
    @param title A title for the plot; it shows up in window title bar
    """
    # Create the main program window and give it a title
    tk_root = tkinter.Tk()
    tk_root.wm_title(title)

    # Create a Matplotlib 
    fig = Figure()
    axes = fig.add_subplot()

    # Create the drawing canvas and a handy plot navigation toolbar
    canvas = FigureCanvasTkAgg(fig, master=tk_root)
    toolbar = NavigationToolbar2Tk(canvas, tk_root, pack_toolbar=False)
    toolbar.update()

    # Create the buttons that run tests, clear the screen, and exit the program
    button_quit = tkinter.Button(master=tk_root,
                                 text="Quit",
                                 command=tk_root.destroy)
    button_clear = tkinter.Button(master=tk_root,
                                  text="Clear",
                                  command=lambda: axes.clear() or canvas.draw())
    button_run = tkinter.Button(master=tk_root,
                                text="Run Step Reponse",
                                command=lambda: plot_function(axes, canvas,
                                                              xlabel, ylabel))
   # button_kp = tkinter.Button(master=tk_root,
                               # text="Run Step Reponse",
                               
                               #command=lambda: plot_function(axes, canvas,
                                #                              xlabel, ylabel))

    # Arrange things in a grid because "pack" is weird
    canvas.get_tk_widget().grid(row=0, column=0, columnspan=3)
    toolbar.grid(row=1, column=0, columnspan=3)
    button_run.grid(row=2, column=0)
    button_clear.grid(row=2, column=1)
    button_quit.grid(row=2, column=2)

    # This function runs the program until the user decides to quit
    tkinter.mainloop()


# This main code is run if this file is the main program but won't run if this
# file is imported as a module by some other main program
if __name__ == "__main__":
    # run the tk_matplot function with the proper plot function and labels
    tk_matplot(step_reponse,
               xlabel='Time [ms]',
               ylabel='Volts [v]',
               title='Simulated and Measured Step Response')
        

