# This is a guide for how to use python package `SimBrain`

## Firstly, you need to import Brain and create an instance of pybrain.

```python

>>> from SimBrain import ParticleSim
>>> myBrain = ParticleSim.SimBrain()

```

Now that an instance of SimBrain has been created under `myBrain` we can get started using the library.

> # Note:
> Please check for the requirements under SimBrain/README.md

## Creating your first `ParticleSimulation`  

In order to use particle, we need to create an instance of it:

```python
>>> myParticle = myBrain.ParticleSimulation("Our_Particle",18.9 ,15.8 ,17.2 ,1.11 ,14.5 ,27.2 ,1.6 ,10.4 ,9.98 )

```

Now we can call any part of the particle easily.

```python

>>> print(myParticle.name)
Our_Particle

```

Alternatively, we could import our data from a csv file (look at the template for help), as follows:

```python

>>> particle_list = myBrain.openDataFromPath("cfmTestSpreadsheet.csv")
>>> print(particle_list[0].getData()) # this will get the first particle in the list
['Example1', 18.9, 15.8, 17.2, 1.11, 14.5, 27.2, 1.6, 10.4, 9.98, 'N/A', 'N/A', 'N/A', 'N/A']

```

Next we can use this to calculate the object's travel:

```python

>>> result = myBrain.calculateFor(0)
>>> x = result[1][0]
>>> z = result[1][2]
>>> print("max height:", max(z))
max height: 0.030960751744567642

```
