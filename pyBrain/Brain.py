import numpy as np
from scipy.integrate import solve_ivp
class PyBrain:
    running = True


    def open_csv(self, path):
        import csv
        data = []
        with open(path) as csv_file:
            csv_read = csv.reader(csv_file, delimiter=',')

            for i in csv_file:
                data.append(i.strip().split(","))

        return data

    class ParticleSimulation:
        # Establish Variables
        drag_coeff = 0.47
        time_in_air, dist_travelled, time_to_max, max_z = "N/A", "N/A", "N/A", "N/A"

        def __init__(self, name: str, u, x, z, angle, mass, diam, air_resistance, air_density, gravity):
            self.name = str(name)
            self.u = float(u)
            self.x = float(x)
            self.z = float(z)
            self.angle = float(angle)
            self.mass = float(mass)
            self.diam = float(diam)
            self.air_resistance = float(air_resistance)
            self.air_density = float(air_density)
            self.gravity = float(gravity)

        def updateResults(self, tx, dx, dz, tz):
            self.time_in_air, self.dist_travelled, self.time_to_max, self.max_z = tx, dx, tz, dz

        def getData(self) -> list:
            return [self.name, self.u, self.x, self.z, self.angle, self.mass,
                    self.diam, self.air_resistance, self.air_density, self.gravity,
                    self.time_in_air, self.max_z]

    particle_list: list[ParticleSimulation] = []

    def import_experiments(self, raw_data:list) ->list[ParticleSimulation]:
        raw_data = raw_data
        print("Raw DATA:", raw_data)
        for i in range(1, len(raw_data)):
            try:
                self.particle_list.append(self.ParticleSimulation(name=raw_data[i][0], u=raw_data[i][1],
                                                                  x=raw_data[i][2], z=raw_data[i][3],
                                                                  angle=raw_data[i][4], mass=raw_data[i][5],
                                                                  diam=raw_data[i][6], air_resistance=raw_data[i][7],
                                                                  air_density=raw_data[i][8], gravity=raw_data[i][9]))
            except Exception as error:
                print('error with data line', i, ':', error)
        return self.particle_list



    # initiate after load
    def openDataFromPath(self,path)->list[ParticleSimulation]:
        print("GO")
        return self.import_experiments(self.open_csv(path))

    # import calculations:
    def calculateFor(self, number: int):
        results = []
        print(self.particle_list)
        print(number)
        particle = self.particle_list[number]

        v0 = ((int(particle.x)**2) * (int(particle.z)**2))**(1/2)
        theta0 = particle.angle
        # starting coords
        x0 = 0
        z0 = 0

        # starting velocities
        v0_x = particle.x
        v0_z = particle.z
        general_speed = np.hypot(int(v0_x), int(v0_z))

        # current variables
        v_x = v0_x
        v_z = v0_z

        # importing particle dimensions/environment from particle class
        v: int
        m = particle.mass
        g = particle.gravity
        crossSection = np.pi * (int(particle.diam)/2)**2
        d = particle.air_density
        c = particle.air_resistance
        Cd = particle.drag_coeff

        starting_values = (0, v0_x, 0, v0_z)

        def speeds_calculation(t, u):
            x = u[0]
            v_x = u[1]
            z = u[2]
            v_z = u[3]

            speed = np.hypot(v_x, v_z)
            a_x = ((-0.5 * Cd * d * crossSection)/m) * speed * v_x
            a_z = ((-0.5 * Cd * d * crossSection)/m) * speed * v_z - g
            return (v_x, a_x, v_z, a_z)

        (t0, tf) = 0, 50

        def hit_ground(t, u):
            return u[2]

        hit_ground.direction = -1
        hit_ground.terminal = True

        def z_max(t, u):
            return u[3]

        solution = solve_ivp(speeds_calculation, (t0, tf),
                             starting_values, dense_output=1, events=(hit_ground, z_max))
        print("Solution =", solution)
        print(solution.t_events[0])
        t = np.linspace(0, solution.t_events[0][0], 100)
        print("times:", t)

        solution_for_t = solution.sol(t)
        print("Returned SOLUTION :", solution_for_t)
        return solution, solution_for_t


mainBrain = PyBrain()
