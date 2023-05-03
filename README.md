# Group Project - Computing For Mathematics:

<https://github.com/Hwezza/cfm2023>

> Submission: 2023
> Group: The Limit Does Not Exist

## Contents

- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#authors">Authors</a>
- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#how-to-use">How to use</a>
- <a href="https://github.com/Hwezza/cfm2023/edit/main/README.md#full-documentation">Full Documentation</a>
  - Class pyBrain


### Authors:

- Harrison Wescott
- George Naunton
- Calvin Pannokaran
- Toby Soden

## How to use

import Brain and create an instance

> from Main.py example program
> ``` python
> import pyBrain.Brain as Brain
> pyBrain = Brain.mainBrain
> ```

## Full documentation:

### Class pyBrain

``` python
class PyBrain:
  ...
```

This class is instanced automatically (upon importing Brain) as mainBrain and can be called as in the example below:

>``` python
>import pyBrain.Brain as Brain
>pyBrain = Brain.mainBrain
>
>pyBrain.open_csv(somePath)
>```

data can be imported from a csv file with `import_data_from_path(path)`, however data must be presented as below:

<img width="678" alt="Screenshot 2023-05-03 at 17 13 16" src="https://user-images.githubusercontent.com/34777353/235976596-b4ec07f6-d7e9-4172-b748-3ab6fb096560.png">
