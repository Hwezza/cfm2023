# Group Project - Computing For Mathematics

<https://github.com/Hwezza/cfm2023>

Find the CFM presentation at

<https://www.dropbox.com/s/45aiygq646txi4v/CFM%20Presentation.mp4?dl=0>

> Submission: 2023  
> Group: The Limit Does Not Exist

### Authors

- Harrison Wescott
- George Naunton
- Calvin Pannokaran
- Toby Soden

### Documentation guide

This readme has the basic outline of using this library
Under docs, you can find *tutorials*, *references*, a deeper dive into *explanations*, some *examples* as well as a *how-to*.

There is also a two page essay under docs

## How to use

Import Brain and create an instance of pybrain

> From Main.py example program:
>
```python

>>> from ParticleSim import SimBrain
>>> myBrain = SimBrain()

```

## How to test

Testing the code:

```cmd

$python ParticleSim_Tests.py

```

Testing the Documentation:

```cmd

$python doc_test.py

```

## Brief documentation

-----

## Class SimBrain

``` python

class SimBrain:
  ...

```

This is the main class of SimBrain an instance can be created

## Method `open_csv`

This function opens a CSV file and returns its contents as a list of lists.

>:param path: The path parameter is a string that represents the file path of the CSV file that
needs to be opened and read
>
>:return: a list of lists, where each inner list represents a row of data from the CSV file. The
data is obtained by reading the CSV file located at the given path and parsing it using the csv
module. The resulting list of lists is then returned.

## Class `ParticleSimulation`

The ParticleSimulation class defines a simulation of a particles flight including it's initial conditions, physical properties, and methods for updating and retrieving results.

Every instance of the ParticleSimulation object has the following variables initialised on creation:

- :param name: A string representing the name of the object being modeled  
- :type name: str  
- :param u: initial velocity of the object  
- :param x: x is a float parameter representing the initial horizontal distance of the
projectile from the origin  
- :param z: z is a float parameter that represents the initial height or altitude of the object
being launched. It is measured in meters  
- :param angle: The angle at which the object is launched or thrown, measured in radians  
- :param mass: The mass of the object in kilograms  
:param diam: diam stands for diameter and is a parameter that represents the diameter of the
object in meters  
- :param air_resistance: Air resistance is the force that opposes the motion of an object
through the air. In this context, it refers to the amount of resistance that the air exerts
on the object as it moves through it.
- :param air_density: The density of the air through which the object is moving. It is
typically measured in kilograms per cubic meter (kg/m^3)
- :param gravity: The acceleration due to gravity, measured in meters per second squared
(m/s^2). It is a constant force that pulls objects towards the center of the planet  

## Method `import_data_from_path`

data can be imported from a csv file with `import_data_from_path(path)`, however data must be presented as below:

<img width="678" alt="Screenshot 2023-05-03 at 17 13 16" src="https://user-images.githubusercontent.com/34777353/235976596-b4ec07f6-d7e9-4172-b748-3ab6fb096560.png">

## Method `import_experiments`

This function imports raw data and creates a list of ParticleSimulation objects based on the data.

The `raw_data` parameter is a list of lists containing raw data for particle simulations that separates each simulation. Each inner list represents a single simulation and contains the following data in order: name, initial velocity
(u), initial horizontal position (x), initial vertical position (z), launch angle (angle), mass,
diameter, air resistance coefficient, air density
:type raw_data: list
:return: a list of ParticleSimulation objects.

For example:

```python

>>> raw_data = myBrain.open_csv("cfmTestSpreadsheet.csv")
>>> temp_particle_list = myBrain.import_experiments(raw_data)
>>> myBrain.particle_list == temp_particle_list
True
>>> print(myBrain.particle_list[0].name)
Example1

```

## Method `openDataFromPath`

This function opens a CSV file from a given path and imports it as a list of ParticleSimulation objects.

The `path` parameter is a string that represents the file path of a CSV file containing data for particle simulations. The `openDataFromPath` method takes this path as input and returns a list of `ParticleSimulation` objects that are created from the data in the CSV file
:return: A list of ParticleSimulation objects.

## Method `calculateFor`

This function calculates the motion of a particle in the presence of air resistance and gravity
and returns the solution and solution for a given time.

:param number: The parameter `number` is an integer representing the index of a particle in a list of particles. This particle will be used to calculate its motion in the presence of air resistance and gravity
:type number: int  
:return: The function `calculateFor` returns two values: `solution`, which is the solution to the system of differential equations for the motion of a particle in the presence of air resistance and gravity, and `solution_for_t`, which is the solution to the system of differential equations
for the motion of the particle at specific times `t`.

```python
>>> from ParticleSim import SimBrain
>>> test_brain = SimBrain()
>>> test_brain.particleList = []
>>> result = test_brain.calculateFor(0)
>>> x = result[1][0]
>>> z = result[1][2]
>>> print("max z =", max(z))
max z = 0.03096075174456763

```

The function updates the results of time in air, distance travelled, time to maximum height, and
            maximum height.

```python
myParticle.updateResults(
    dx=x[-1],
    tx=result[0].t_events[0][0],
    dz=max(z),
    tz=result[0].t_events[1][0],
)
```

The parameter `dx` is the distance travelled in the x-direction by the partcle
The parameter ``tx` is the time that the particle was in the air until the colision with the ground
The parameter `dz` is the maximum height achieved by the particle
The parameter `tz` is the time taken for the particle to hit the maximum height
