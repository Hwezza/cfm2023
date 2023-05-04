# This is a guide for how to use python package `pyBrain`

## Firstly, you need to import Brain and create an instance of pybrain.

```python
import pybrain.Brain as Brain
myBrain = Brain.Pybrain()
```
> Alternatively, you can use an instance of PyBrain stored in Brain, if you would prefer.  
> This can be done as shown below:
> ```python
> import pybrain.Brain as Brain
> myBrain = Brain.mainbrain
> ```
> In this case the pyBrain object `mainbrain` is stored in the pyBrain.Brain module, making it easier to access from multiple libraries, avoiding circular imports.  

Now that an instance of Pybrain has been created under `myBrain` we can get started using the library.

> # Note:
> Please check for the requirements under README.md

## Creating your first `ParticleSimulation`  

In order to use particle 