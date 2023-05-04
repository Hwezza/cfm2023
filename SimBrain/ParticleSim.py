import numpy as np
from scipy.integrate import solve_ivp


class SimBrain:
    running = True

    def open_csv(self, path):
        """
        This function opens a CSV file and returns its contents as a list of lists.

        :param path: The path parameter is a string that represents the file path of the CSV file that
        needs to be opened and read
        :return: a list of lists, where each inner list represents a row of data from the CSV file. The
        data is obtained by reading the CSV file located at the given path and parsing it using the csv
        module. The resulting list of lists is then returned.
        """
        import csv

        data = []
        with open(path) as csv_file:
            csv_read = csv.reader(csv_file, delimiter=",")

            for i in csv_file:
                data.append(i.strip().split(","))

        return data

    # The `ParticleSimulation` class defines a simulation of a particle's flight, including its
    # initial conditions, physical properties, and methods for updating and retrieving results.
    class ParticleSimulation:
        # Establish Variables
        drag_coeff = 0.47
        time_in_air, dist_travelled, time_to_max, max_z = "N/A", "N/A", "N/A", "N/A"

        def __init__(
            self,
            name: str,
            u,
            x,
            z,
            angle,
            mass,
            diam,
            air_resistance,
            air_density,
            gravity,
        ):
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
            """
            The function updates the results of time in air, distance travelled, time to maximum height, and
            maximum height.

            :param tx: The time the object spent in the air
            :param dx: The distance travelled by an object in the x-direction
            :param dz: dz is the maximum height reached by an object during its flight. It is one of the
            parameters used to update the results of an object's flight
            :param tz: The parameter `tz` likely stands for "time to reach maximum height" and represents the
            amount of time it takes for the object to reach its maximum height during its flight
            """
            self.time_in_air, self.dist_travelled, self.time_to_max, self.max_z = (
                tx,
                dx,
                tz,
                dz,
            )

        def getData(self) -> list:
            """
            The function `getData` returns a list of attributes for an object.
            :return: A list containing the values of various attributes of an object, including its name,
            position, angle, mass, diameter, air resistance, air density, gravity, time in air, and maximum
            height reached.
            """
            return [
                self.name,
                self.u,
                self.x,
                self.z,
                self.angle,
                self.mass,
                self.diam,
                self.air_resistance,
                self.air_density,
                self.gravity,
                self.time_in_air,
                self.max_z,
            ]

    particle_list: list[ParticleSimulation] = []

    def import_experiments(self, raw_data: list) -> list[ParticleSimulation]:
        """
        This function imports raw data and creates a list of ParticleSimulation objects based on the
        data.

        :param raw_data: A list of lists containing raw data for particle simulations. Each inner list
        represents a single simulation and contains the following data in order: name, initial velocity
        (u), initial horizontal position (x), initial vertical position (z), launch angle (angle), mass,
        diameter, air resistance coefficient, air density
        :type raw_data: list
        :return: a list of ParticleSimulation objects.
        """
        raw_data = raw_data
        print("Raw DATA:", raw_data)
        for i in range(1, len(raw_data)):
            try:
                self.particle_list.append(
                    self.ParticleSimulation(
                        name=raw_data[i][0],
                        u=raw_data[i][1],
                        x=raw_data[i][2],
                        z=raw_data[i][3],
                        angle=raw_data[i][4],
                        mass=raw_data[i][5],
                        diam=raw_data[i][6],
                        air_resistance=raw_data[i][7],
                        air_density=raw_data[i][8],
                        gravity=raw_data[i][9],
                    )
                )
            except Exception as error:
                print("error with data line", i, ":", error)
        return self.particle_list

    # initiate after load
    def openDataFromPath(self, path) -> list[ParticleSimulation]:
        """
        This function opens a CSV file from a given path and imports it as a list of ParticleSimulation
        objects.

        :param path: The `path` parameter is a string that represents the file path of a CSV file containing
        data for particle simulations. The `openDataFromPath` method takes this path as input and returns a
        list of `ParticleSimulation` objects that are created from the data in the CSV file
        :return: A list of ParticleSimulation objects.
        """
        return self.import_experiments(self.open_csv(path))

    # import calculations:
    def calculateFor(self, number: int):
        """
        This function calculates the motion of a particle in the presence of air resistance and gravity
        and returns the solution and solution for a given time.

        :param number: The parameter `number` is an integer representing the index of a particle in a
        list of particles. This particle will be used to calculate its motion in the presence of air
        resistance and gravity
        :type number: int
        :return: The function `calculateFor` returns two values: `solution`, which is the solution to the
        system of differential equations for the motion of a particle in the presence of air resistance
        and gravity, and `solution_for_t`, which is the solution to the system of differential equations
        for the motion of the particle at specific times `t`.
        """
        results = []
        print(self.particle_list)
        print(number)
        particle = self.particle_list[number]

        v0 = ((int(particle.x) ** 2) * (int(particle.z) ** 2)) ** (1 / 2)
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
        crossSection = np.pi * (int(particle.diam) / 2) ** 2
        d = particle.air_density
        c = particle.air_resistance
        Cd = particle.drag_coeff

        starting_values = (0, v0_x, 0, v0_z)

        def speeds_calculation(t, u):
            """
            The function calculates the speed and acceleration of an object based on its initial velocity and
            time.

            :param t: It is a variable representing time
            :param u: The parameter u is a tuple containing the initial values of the horizontal position (x),
            horizontal velocity (v_x), vertical position (z), and vertical velocity (v_z) of an object
            :return: The function `speeds_calculation` returns a tuple containing the values of `v_x`, `a_x`,
            `v_z`, and `a_z`.
            """
            x = u[0]
            v_x = u[1]
            z = u[2]
            v_z = u[3]

            speed = np.hypot(v_x, v_z)
            a_x = ((-0.5 * Cd * d * crossSection) / m) * speed * v_x
            a_z = ((-0.5 * Cd * d * crossSection) / m) * speed * v_z - g
            return (v_x, a_x, v_z, a_z)

        (t0, tf) = 0, 50

        def hit_ground(t, u):
            return u[2]

        hit_ground.direction = -1
        hit_ground.terminal = True

        def z_max(t, u):
            return u[3]

        # `solve_ivp` is a function from the `scipy.integrate` module that solves initial value
        # problems (IVPs) for systems of first-order ordinary differential equations (ODEs). In this
        # case, it is being used to solve for the motion of a particle in the presence of air
        # resistance and gravity.
        solution = solve_ivp(
            speeds_calculation,
            (t0, tf),
            starting_values,
            dense_output=1,
            events=(hit_ground, z_max),
        )
        t = np.linspace(0, solution.t_events[0][0], 100)

        solution_for_t = solution.sol(t)
        print("Returned SOLUTION :", solution_for_t)
        return solution, solution_for_t


mainBrain = SimBrain()
