import gui
import numpy as np
from scipy.integrate import solve_ivp

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
        drag_coeff = 0.47
        def __init__(self, name: str, u: int, x:int, z:int, angle:int, mass:int, diam:int, air_resistance:int, air_density:int, gravity:int):
            self.name:str = name
            self.u:int = u
            self.x:int = x
            self.z:int = z
            self.angle:int = angle
            self.mass:int = mass
            self.diam:int = diam
            self.air_resistance:int = air_resistance
            self.air_density:int = air_density
            self.gravity:int = gravity
        

    
    particle_list: list[ParticleSimulation] = []

    def import_experiments(self):
        raw_data = self.raw_data
        print("Raw DATA:", raw_data)
        for i in range(1,len(raw_data)):
            try:
                self.particle_list.append(self.ParticleSimulation(name = raw_data[i][0], u = raw_data[i][1],
                                                                x = raw_data[i][2], z = raw_data[i][3],
                                                                angle = raw_data[i][4], mass = raw_data[i][5],
                                                                diam = raw_data[i][6], air_resistance = raw_data[i][7], 
                                                                air_density = raw_data[i][8], gravity = raw_data[i][9]))
            except:
                print('error with data line',i)
    
        print("Particle LIST:",self.particle_list)

    def startup(self):
        self.open_csv()
        self.import_experiments()
    
    #insert calculations:
    def calculateFor(self, number:int):
        results = []
        particle = self.particle_list[number]

        v0 = ((particle.x**2) * (particle.z**2))**(1/2)
        theta0 = particle.angle
        #starting coords
        x0 = 0
        z0 = 0

        #starting velocities
        v0_x = particle.x
        v0_z = particle.z
        general_speed = np.hypot(v0_x, v0_z)

        # current variables
        v_x = v0_x
        v_z = v0_z


        #particle dimensions/environment
        v: int
        m = particle.mass
        g = particle.gravity
        crossSection = np.pi * (particle.diam/2)**2
        d = particle.air_density
        c = particle.air_resistance
        Cd = particle.drag_coeff

        starting_values = (0, v0_x, 0, v0_z)
        
        def speeds_calculation(t,u):
                x = u[0]
                v_x = u[1]
                z = u[2]
                v_z = u[3]

                speed = np.hypot(v_x, v_z)
                a_x = ((-0.5 * Cd * d * crossSection)/m) * speed * v_x
                a_z = ((-0.5 * Cd * d * crossSection)/m) * speed * v_z - g
                return (v_x, a_x, v_z, a_z)
            
        (t0, tf) = 0, 120

        def hit_ground(t, u):
            return u[2]

        hit_ground.terminal = True
        hit_ground.driection = -1

        def z_max(t,u):
            return u[3]
        
        solution = solve_ivp(speeds_calculation, (t0,tf), starting_values, dense_output=1, events=(hit_ground, z_max))

        times = np.linspace(0, solution.t_events[0][0], 150)

        solution_for_t = solution.solution_for_t(times)
        return solution_for_t


        ## to evaluate
        '''
        particle.a_x == (((-particle.air_density * particle.air_resistance * particle.crossSection)
                               * np.sqrt(particle.xdot**2 + particle.zdot**2))/particle.mass) * particle.xdot
        particle.a_z == ((((-particle.air_density * particle.air_resistance * particle.crossSection)
                               * np.sqrt(particle.xdot**2 + particle.zdot**2))/particle.mass)* particle.zdot
                                 - (particle.mass*particle.gravity))
        '''

    '''
    def speedsAndAccelerations(t, speeds):
        self.particle.a_x = (-0.5 * Cd * d * crossSection * u *)

        solution = solve_ivp()
    '''

        ###

mainBrain = PyBrain()