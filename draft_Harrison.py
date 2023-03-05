import numpy as np
import Brain
pyBrain = Brain.PyBrain()


particle1 = pyBrain.ParticleSimulation(name = 'one', u = 1, x=1, z=1, angle=1,mass=5,diam=5,air_resistance=0.5,air_density=1.28,gravity=9.8)

print(particle1.name)