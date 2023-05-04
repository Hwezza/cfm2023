# This is a guide for building the code, step by step

## Firstly, you need to import Brain and create an instance of pybrain.
This tutorial will assume a basic understanding and use of matplotlib and tkinter.

```python
from SimBrain import SimBrain
myBrain = SimBrain()
```
Now you have imported SimBrain we also will need to import matplotlib and tkinter to our system.

```
import matplotlib as mtplt
from matplotlib import pyplot
import tkinter
from tkinter import ttk
```

```
class guibrain:
    mainBrain = None

    program1_window: tkinter.Tk
    choiceWindow: tkinter.Tk
    main_window: tkinter.Tk
    tree: ttk.Treeview
```
Now we have imported all of tkinter and matplotlib, we can now create  menu, this will be the base programme for presenting the data that the user has created, here you can rename your menu and adjust the size of it in `main_window.title("Home")` and `main_window.geometry("800x450")`.
```
def open_menu(self):
        main_window = tkinter.Tk(
            screenName=None, baseName=None, className="Window", useTk=1
        )
        main_window.title("Home")
        main_window.geometry("800x450")
```
The first step to creating a working menu will be to add a button. Our button now takes us to the menu with the users data and examples.

The Command `self.open_choice_window` then opens a specified window that has been selected.
```
first_option = tkinter.Button(
            main_window,
            text="Particle\nCatapult",
            width=10,
            height=5,
            command=self.open_choice_window,
        )
```
This next step now adds the placement of the button in our menu as well as including the ability to customise it based on user preference
```
first_option.place(x=20, y=20)
        first_label = tkinter.Label(
            main_window,
            text="Particle catapult:\nSimulating flight of a particle from a catapult.",
            width=60,
            height=5,
            background="grey",
        )
        first_label.place(x=180, y=20)
        main_window.mainloop()
```
Here the user can pull numbers from a spreadsheet and import it into our programme for use.
```
def open_choice_window(self):
        self.choiceWindow = tkinter.Tk(
            screenName=None, baseName=None, className="Window", useTk=1
        )
        self.choiceWindow.title("Particle Simulation")
        self.choiceWindow.geometry("800x450")

        self.tree = ttk.Treeview(
            self.choiceWindow,
            columns=(self.mainBrain.open_csv("cfmTestSpreadsheet.csv")[0]),
            show="headings",
        )
```
The data here is pulled from the spreadsheet and printed in the menu in a separate data table with the addition of all necessary headings of the columns.
```
def write_tree_headings(self):
        raw_data = self.mainBrain.open_csv("cfmTestSpreadsheet.csv")
        print(raw_data)

        columns = raw_data[0] + ["Time in air"] + ["Max Height"]
        print("columns =", columns)

        self.tree = ttk.Treeview(self.choiceWindow, columns=columns, show="headings")
        i = 0
        for heading in columns:
            print("HEADING: ", heading)
            self.tree.heading(heading, text=str(heading))
            i += 1
            self.tree.column(heading, width=50)
        self.tree.column(raw_data[0][0], width=100)
```

Using show_data, we can display the data that has been inputted by the user to view along with the defining number of each projectile. This will be prited on the menu.
```
def show_data(self, number: int):
        selected_particle = self.mainBrain.particle_list[number]
        print(selected_particle)
```

Using the particle list that was created we define write_experiments_to_tree which will pull the different experiment and place them in the displayed table of data.

```
 def write_experiments_to_tree(self):
        print("Writting to tree:")
        print(self.mainBrain.particle_list)
        self.tree.delete(*self.tree.get_children())
        i = 0
        for experiment in self.mainBrain.particle_list:
            print("experiment", i + 1, ":", experiment.name)
            self.tree.insert("", tkinter.END, values=(experiment.getData()), iid={i})
            i += 1
```
Now we have the data displayed in a table we can start to form a graph that displays the outcome, first, we have to calculate our x and z values (horizontal and vertical distance respectively). These will be calulated from our table of data then using `pyplot.plot(x,z)` a graph will be formed to show the trajectory and distance of our particle.

This system also will allow you to customise the axis titles and labels of the graph to suit the user. Finally, `print("graph displayed")` will show our fully annotated graph.
```
def selected_experiment(self):
        print("selection: ", self.tree.selection()[0])

        result = self.mainBrain.calculateFor(int(self.tree.selection()[0][1]))
        x = result[1][0]
        z = result[1][2]
        print("graphing")
        mtplt.use("TkAgg")
        pyplot.plot(x, z)
        print("Update Results:")
        self.mainBrain.particle_list[int(self.tree.selection()[0][1])].updateResults(
            dx=x[-1],
            tx=result[0].t_events[0][0],
            dz=max(z),
            tz=result[0].t_events[1][0],
        )
        print("results updated")
        self.write_experiments_to_tree()
        print("Written to tree")
        pyplot.xlabel("Distance (m)")
        pyplot.ylabel("Height (m)")
        pyplot.title("Particle Graph")

        pyplot.show()
        print("graph displayed")
```
