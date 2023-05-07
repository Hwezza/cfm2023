# A breif overview of how to use `SimBrain`

## First import the library and create an instance of the SimBrain

```python
>>> from SimBrain import SimBrain
>>> myBrain = SimBrain()

```

This creates an instance of SimBrain which is saved as myBrain, allowing us to start using the library.

## Creating a `ParticleSimulation`

First we need to define a particle with all the data that is necessary in the calculations. To do so we use the format,

```python

myParticle = myBrain.ParticleSimulation(name, u, x, z, angle, mass, diam, air res, air dens, grav)

```

In this tutorial we will use the particle,

```python

>>> myParticle = myBrain.ParticleSimulation("Our_particle", 10, 8, 6, 0.52, 5, 2, 1.2, 5.6,  9.81)

```

> ## Note
>
>The angle must be in radians for the program to work as we are doing caclulus. The x and z velocities don't matter right now. It's been left open for future developments, or if you want to work with those components.

Now we can call any parameter of our particle; such as,

```python
>>> print(myParticle.name)
Our_particle

```

After defining the particle we have to add it to SimBrain's particle list;

```python

>>> myBrain.particle_list.append(myParticle)

```

Now we can perform calculations by running,

```python

>>> result = myBrain.caclulateFor(0)

```

> # Note
>
> 0 is the index for our particle.

To save the results we need to do,

```python

>>> result = myBrain.calculateFor(0)
>>> x = result[1][0]
>>> z = result[1][2]
>>> myBrain.particle_list[0].updateResults(
...    dx=x[-1], 
...    tx=result[0].t_events[0][0],
...    dz=max(z),
...    tz=result[0].t_events[1][0],
)

```

 This is updating the results as the simulation happens. In the simultation it contains the distance travelled horiztonally, max height, time taken to reach the ground and time take to reach max height. The above code gives the x,z values at any given time(t). The dx is the horizontal distance before hitting the ground, tx is time taken to reach the ground, and tz is the time taken to reach the max height

These can be outputted through,

```python

>>> print(myBrain.particle_list[0].getData())
['Our_particle', 10.0, 8.0, 6.0, 0.52, 5.0, 2.0, 1.2, 5.6, 9.81, 'N/A', 'N/A', 'N/A', 'N/A']

```

The output is in the following format:
 (name, u, x, z, angle, mass, diam, air res, air dens, grav, time in air, distance travelled(x), time to max height, max height)
