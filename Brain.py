import gui
class PyBrain:
    running = True
    
    def menu(self):
        gui.open_menu()
    
    def option1_selected(self):
        print("open option1")
        gui.open_program1
    
    def open_csv() -> list:
        import csv
        data = []
        with open('cfmtestSpreadsheet.csv') as csv_file:
            csv_read=csv.reader(csv_file, delimiter=',')

            for i in csv_file:
                data.append(i.strip().split(","))
            
        return data




    class ParticleSimulation:
        #Establish Variables
        def __init__(self, name, u, x, z, angle, mass, diam, air_resistance, air_density, gravity, xdot, xdotdot, zdot, zdotdot):
            self.name = name
            self.u = u
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
        
        #calculations:
        ###

    def import_experiments(raw_data) -> list:
        particle_list = []
        for i in range(len(raw_data)):
            print(particle_list)
            particle_list.append(ParticleSimulation(name = raw_data[i][0], u =raw_data[i][1], angle = raw_data[i][2], mass = raw_data[i][3],
                                                    diam = raw_data[i][4], air_resistance = raw_data[i][5], 
                                                    air_density = raw_data[i][6], gravity = raw_data[i][7]))
        return particle_list

    '''
    req variables:
    Name
    u
    Angle
    Mass
    Air resistance coeff
    Air density
    Gravity
    '''

    #testing
    '''
    brain = PyBrain()
    brain.menu()
    '''