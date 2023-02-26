import gui
class PyBrain:
    running = True
    
    def menu(self):
        gui.open_menu()
    
    def option1_selected(self):
        print("open option1")
        gui.open_program1


class ParticleSimulation:
    #Establish Variables
    def __init__(name, u, angle, mass, air_resistance, air_density, gravity):
        self.name = name
        self.u = u
        self.angle = angle
        self.mass = mass
        self.air_resistance = air_resistance
        self.air_density = air_density
        self.gravity = gravity
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