# Group Project - Computing For Mathematics:

<https://github.com/Hwezza/cfm2023>

> Submission: 2023  
> Group: The Limit Does Not Exist

## Contents

- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#authors">Authors</a>
- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#how-to-use">How to use</a>
- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#full-documentation">Full Documentation</a>
  - <a href = "https://github.com/Hwezza/cfm2023/edit/main/README.md#Class-Pybrain">Class pyBrain</a>


### Authors:

- Harrison Wescott
- George Naunton
- Calvin Pannokaran
- Toby Soden

## How to use

Import Brain and create an instance of pybrain

> From Main.py example program:
> ``` python
> import pyBrain.Brain as Brain
> pyBrain = Brain.mainBrain
> ```

## How to test

Testing the code:

```
$ python Brain_Tests.py
```

Testing the Documentation:

```
$ python -m doctest README.md
```

## Brief documentation:
-----

## Class SimBrain

``` python
>>>class SimBrain:
  ...
```
this is the main class of SimBrain

## Method `open_csv`
This function opens a CSV file and returns its contents as a list of lists.

>:param path: The path parameter is a string that represents the file path of the CSV file that
needs to be opened and read

>:return: a list of lists, where each inner list represents a row of data from the CSV file. The
data is obtained by reading the CSV file located at the given path and parsing it using the csv
module. The resulting list of lists is then returned.

# Class `ParticleSimulation`

The ParticleSimulation class defines a simulation of a particles flight including it's initial conditions, physical properties, and methods for updating and retrieving results.

Every instance of the ParticleSimulation object has the following variables initialised on creation:


- :param name: A string representing the name of the object being modeled  
- :type name: str  
- :param u: initial velocity of the object  
- :param x: x is a float parameter representing the initial horizontal distance of the
projectile from the origin  
- :param z: z is a float parameter that represents the initial height or altitude of the object
being launched. It is measured in meters  
- :param angle: The angle at which the object is launched or thrown, measured in degrees  
- :param mass: The mass of the object in kilograms  
:param diam: diam stands for diameter and is a parameter that represents the diameter of the
object in meters  
- :param air_resistance: Air resistance is the force that opposes the motion of an object
through the air. In this context, it refers to the amount of resistance that the air exerts
on the object as it moves through it.
- :param air_density: The density of the air through which the object is moving. It is
typically measured in kilograms per cubic meter (kg/m^3) 
- :param gravity: The acceleration due to gravity, measured in meters per second squared
(m/s^2). It is a constant force that pulls objects towards the center of the Earth  






## Method `import_data_from_path`

data can be imported from a csv file with `import_data_from_path(path)`, however data must be presented as below:

<img width="678" alt="Screenshot 2023-05-03 at 17 13 16" src="https://user-images.githubusercontent.com/34777353/235976596-b4ec07f6-d7e9-4172-b748-3ab6fb096560.png">
