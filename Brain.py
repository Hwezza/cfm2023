import gui
import numpy as np
from tkinter.messagebox import showinfo

class PyBrain:
    running = True
    raw_data = []
    Gui = gui.guibrain()

    def menu(self):
        self.Gui.open_menu()
    
    def option1_selected(self):
        #print("open option1")
        self.Gui.open_program1
    
    def open_csv(self):
        import csv
        data = []
        with open('cfmtestSpreadsheet.csv') as csv_file:
            csv_read=csv.reader(csv_file, delimiter=',')

            for i in csv_file:
                data.append(i.strip().split(","))
            
        self.raw_data = data




    class ParticleSimulation:
        #Establish Variables
        def __init__(self, name, x, z, angle, mass, diam, air_resistance, air_density, gravity, xdot, xdotdot, zdot, zdotdot):
            self.name = name
            self.x = x
            self.z = z
            self.angle = angle
            self.mass = mass
            self.diam = diam
            self.air_resistance = air_resistance
            self.air_density = air_density
            self.gravity = gravity
            self.xdot = xdot
            self.xdotdot = xdotdot
            self.zdot = zdot
            self.zdotdot = zdotdot
        

    
    particle_list: list[ParticleSimulation] = []

    def import_experiments(self):
        raw_data = self.raw_data
        print("Raw DATA:", raw_data)
        for i in range(1,len(raw_data)):
            self.particle_list.append(self.ParticleSimulation(name = raw_data[i][0], 
                                                            x = raw_data[i][2], z = raw_data[i][3],
                                                            angle = raw_data[i][4], mass = raw_data[i][5],
                                                            diam = raw_data[i][6], air_resistance = raw_data[i][7], 
                                                            air_density = raw_data[i][8], gravity = raw_data[i][9]))
        print("Particle LIST:",self.particle_list)

    def startup(self):
        self.open_csv()
        self.import_experiments()
    
    #insert calculations:
    def calculateFor(self, number:int):
        results = []
        particle = self.particle_list[number]
        '''

        m = particle.mass
        g = particle.gravity
        crossSection = np.pi * (particle.diam/2)**2
        p = particle.air_density
        ## to complete
        '''
        showinfo(title='Object Picked', message=("Object picked:",particle.name))

        return results
        ###

mainBrain = PyBrain()