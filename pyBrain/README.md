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

## Brief documentation:
-----

## Class pyBrain

``` python
class PyBrain:
  ...
```

This class is instanced automatically (upon importing Brain) as mainBrain and can be called as in the example below:

``` python
import pyBrain.Brain as Brain
pyBrain = Brain.mainBrain

# This can now be used as follows
pyBrain.open_csv(somePath)
```

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

>params:

>name: string  
>u: float  
>x: float  
>z: float  
>angle: float  





## Method `import_data_from_path`

data can be imported from a csv file with `import_data_from_path(path)`, however data must be presented as below:

<img width="678" alt="Screenshot 2023-05-03 at 17 13 16" src="https://user-images.githubusercontent.com/34777353/235976596-b4ec07f6-d7e9-4172-b748-3ab6fb096560.png">
