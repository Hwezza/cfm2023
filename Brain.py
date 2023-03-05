import gui


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
        def __init__(self, name, u, x, z, angle, mass, diam, air_resistance, air_density, gravity):
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
        
        #insert calculations:
        def calculate():

            return
        ###
    
    particle_list: list[ParticleSimulation] = []

    def import_experiments(self):
        raw_data = self.raw_data
        print("Raw DATA:", raw_data)
        for i in range(1,len(raw_data)):
            self.particle_list.append(self.ParticleSimulation(name = raw_data[i][0], u =raw_data[i][1], 
                                                            x = raw_data[i][2], z = raw_data[i][3],
                                                            angle = raw_data[i][4], mass = raw_data[i][5],
                                                            diam = raw_data[i][6], air_resistance = raw_data[i][7], 
                                                            air_density = raw_data[i][8], gravity = raw_data[i][9]))
        print("Particle LIST:",self.particle_list)

    def startup(self):
        self.open_csv()
        self.import_experiments()

mainBrain = PyBrain()