from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from random import choice
import numpy as np
import tkinter as tk


class BrownianMotion:

    def open_window(self):
        '''
        This function creates the window showing the plot of the simulation.
        It contains the
            * definition of buttons und labels with tkinter,
            * methods for user input
            * call of method for the random walk
            * methods for plotting the obtained coordinates
        '''
        fig = Figure(figsize=(8, 8), facecolor="white")     
        root = tk.Tk()                                      
        root.title("Brownian Motion")                       

        canvas = FigureCanvasTkAgg(fig, master=root)        
        canvas.get_tk_widget().grid(row=0, column=2, sticky=tk.W)

        axis = fig.add_subplot(111, projection="3d", position=(0.125, 0.11, 0.775, 0.77))    
        axis.set_xlabel("x axis [a.U.]")
        axis.set_ylabel("y axis [a.U.]")
        axis.set_zlabel("z axis [a.U.]")
        axis.set_title("Brownian Motion Simulated By Random Walk", fontsize=18)

        toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)    
        toolbar.update()
        toolbar.grid(row=0, column=2, sticky=tk.N + tk.W + tk.E)

        def plot_2D():
            '''
            This method plots the Brownian Motion in 2D.
            '''
            data_x, data_y = get_parameters()

            for i in range(len(data_x)):
                axis.scatter(data_x[i], data_y[i])      
                axis.scatter(0, 0, s=500, c="k")        
                axis.plot(data_x[i], data_y[i], '--')   
                                                        
            canvas.draw()


        def plot_3D():
            '''
            This method plots the Brownian Motion in 3D.
            '''
            data_x, data_y, data_z = get_parameters()

            for i in range(len(data_x)):
                axis.scatter(data_x[i], data_y[i], data_z[i])      
                axis.scatter(0, 0, s=500, c="k")                   
                axis.plot(data_x[i], data_y[i], data_z[i], '--')   
                                                                   
            canvas.draw()


        def clear_plot():
            '''
            This method deletes the plot.
            '''
            axis.cla()                         
            axis.set_title("Brownian Motion Simulated By Random Walk", fontsize=18)
            axis.set_xlabel("x axis [a.U.]")  
            axis.set_ylabel("y axis [a.U.]")  
            axis.set_zlabel("z axis [a.U.]")  
            canvas.draw()


        def clear_all():
            '''
            This method deletes the plot and the entered parameters.
            '''
            i_1.set("0")    # No. of steps
            i_2.set("0")    # No. of particles
            i_3.set("0")    # Maximum step size
            axis.cla()      # clear axis
            axis.set_title("Brownian Motion Simulated By Random Walk", fontsize=18)
            axis.set_xlabel("x axis [a.U.]")   
            axis.set_ylabel("y axis [a.U.]")   
            axis.set_zlabel("z axis [a.U.]")   
            canvas.draw()


        def get_parameters():
            '''
            This methods reads in the entries of the spin boxes and passed to method random_walker().
            '''
            num_steps = int(e_steps.get())      # No. of steps
            num_particles = int(e_part.get())   # No. of particles
            step_size = int(e_size.get())       # Maximum step size

            data_x, data_y, data_z = random_walker(num_particles, num_steps, step_size)

            return data_x, data_y, data_z

        f1 = tk.Frame(root)
        f1.grid(row=0, column=0, sticky=tk.N)  

        param = tk.Label(f1, text="Parameters", font=("default", 18, 'bold'), relief="groove", bg="grey")
        param.grid(row=1, column=0, columnspan=2, sticky=tk.N + tk.W + tk.E)

        i_1 = tk.IntVar()    # No. of steps
        i_2 = tk.IntVar()    # No. of particles
        i_3 = tk.IntVar()    # Maximum step size

        steps = tk.Label(f1, text="Number of Steps: ", font=("default", 14))
        steps.grid(row=2, column=0, sticky=tk.N + tk.W)
        i_1.set("0")
        e_steps = tk.Spinbox(f1, from_=0, increment=100, to=5000, bd=3, font=("default", 14), textvariable=i_1)
        e_steps.grid(row=3, column=0)

        part = tk.Label(f1, text="Number of Particles: ", font=("default", 14))
        part.grid(row=4, column=0, sticky=tk.N + tk.W)
        e_part = tk.Spinbox(f1, from_=0, to=10, bd=3, font=("default", 14), textvariable=i_2)
        e_part.grid(row=5, column=0)

        dist = tk.Label(f1, text="Maximum Step Size: ", font=("default", 14))
        dist.grid(row=6, column=0, sticky=tk.N + tk.W)
        e_size = tk.Spinbox(f1, from_=0, to=10, bd=3, font=("default", 14), textvariable=i_3)
        e_size.grid(row=7, column=0)

        dist = tk.Label(f1, text="Plot Options", font=("default", 18, 'bold'), relief="groove", bg="grey")
        dist.grid(row=9, column=0, columnspan=2, sticky=tk.N + tk.W + tk.E)

        b_plot_1 = tk.Button(f1, text="Plot 2D", command=plot_2D, font=("default", 14))
        b_plot_1.grid(row=10, column=0, columnspan=2, sticky=tk.N + tk.W + tk.E)

        b_plot_2 = tk.Button(f1, text="Plot 3D", command=plot_3D, font=("default", 14))
        b_plot_2.grid(row=11, column=0, columnspan=2, sticky=tk.N + tk.W + tk.E)

        dist = tk.Label(f1, text="Clear Options", font=("default", 18, 'bold'), relief="groove", bg="grey")
        dist.grid(row=12, column=0, columnspan=2, sticky=tk.N + tk.W + tk.E)

        b_clear = tk.Button(f1, text="Clear Plot", command=clear_plot, font=("default", 14))
        b_clear.grid(row=13, column=0, sticky=tk.N + tk.W + tk.E)

        b_clear = tk.Button(f1, text="Clear All", command=clear_all, font=("default", 14), bg="red")
        b_clear.grid(row=14, column=0, sticky=tk.N + tk.W + tk.E)

        b_quit = tk.Button(root, text="Quit", command=quit, font=("default", 14))
        b_quit.grid(row=0, column=0, sticky=tk.S+tk.W+tk.E)

        root.mainloop()


def random_walker(num_particles, num_steps, step_size):
    '''
    This methods implements the random walk.
    '''
    data_x = []    
    data_y = []    
    data_z = []                     

    for particle in range(num_particles):  
                                        
        x_coord = [0] 
        y_coord = [0] 
        z_coord = [0] 

        while len(x_coord) < num_steps:    
                                           
            x_direction = choice([-1, 1])                              
            x_distance = choice(list(np.arange(0, step_size, .1)))     
            x_step = x_direction * x_distance                          

            y_direction = choice([-1, 1])                              
            y_distance = choice(list(np.arange(0, step_size, .1)))     
            y_step = y_direction * y_distance                          

            z_direction = choice([-1, 1])                              
            z_distance = choice(list(np.arange(0, step_size, .1)))     
            z_step = z_direction * z_distance                          


            if x_step == 0 and y_step == 0 and z_step == 0:            
                continue                                               

            x = x_coord[-1] + x_step   
            y = y_coord[-1] + y_step   
            z = z_coord[-1] + z_step   

            x_coord.append(x)   
            y_coord.append(y)   
            z_coord.append(z)

        data_x.append(x_coord)  
        data_y.append(y_coord)  
        data_z.append(z_coord)  

    return data_x, data_y, data_z


if __name__ == "__main__":
    bm = BrownianMotion()    
    bm.open_window()         