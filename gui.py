import tkinter
from tkinter import ttk
import matplotlib as mtplt


### Main window
class guibrain:
    program1_window: tkinter.Tk
    choiceWindow: tkinter.Tk
    tree : ttk.Treeview
    def open_menu(self):
        main_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
        main_window.title("Home")
        main_window.geometry("800x450")

        # choices:
        first_option = tkinter.Button(main_window, text = "Particle\nCatapult", width = 10, height = 5, command = self.open_choice_window)
        first_option.place(x=20,y=20)
        first_label = tkinter.Label(main_window, text= "Particle catapult:\nSimulating flight of a particle from a catapult.",
                                    width = 60, height = 5, background= "grey")
        first_label.place(x=180, y=20)
        main_window.mainloop()


    ### Program 1 (ParticleSim)
    '''
    def open_program1(self):
        self.program1_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
        self.program1_window.title("Particle Simulation")
        self.program1_window.geometry("800x450")

        start_button = tkinter.Button(self.program1_window, text = "Start!", width = 10, height = 5, command = self.show_data, background="grey")
        start_button.place(x = 20, y = 20)

        self.program1_window.mainloop()
    '''

    def show_data(number: int):
        from Brain import mainBrain
        selected_particle = mainBrain.particle_list[number]
        print(selected_particle)
    
    def write_experiments_to_tree(self):
        from Brain import mainBrain
        print("Writting to tree:")
        print(mainBrain.particle_list)
        self.tree.delete(*self.tree.get_children())
        i = 0
        for experiment in mainBrain.particle_list:
            print("experiment",i+1,":",experiment.name)
            self.tree.insert('', tkinter.END, values=(experiment.getData()),iid={i})
            i+=1  
    #click
    def selected_experiment(self):
        print("selection: ",self.tree.selection()[0])
        from Brain import mainBrain
        result = mainBrain.calculateFor(int(self.tree.selection()[0][1]))
        x = result[1][0]
        z = result[1][2]
        print("graphing")
        mtplt.use('TkAgg')
        mtplt.pyplot.plot(x,z)
        print("Update Results:")
        mainBrain.particle_list[int(self.tree.selection()[0][1])].updateResults(dx = x[-1], tx = result[0].t_events[0][0], dz = max(z), tz = result[0].t_events[1][0])
        print("results updated")
        self.write_experiments_to_tree()
        print("Written to tree")
        mtplt.pyplot.show()
        print("graph displayed")

        
    def write_tree_headings(self):
        from Brain import mainBrain
        mainBrain.raw_data[0] += ["Time in Air", "Max Height"]
        columns = (mainBrain.raw_data[0])
        print("columns =",columns)

        self.tree = ttk.Treeview(self.choiceWindow, columns=columns, show='headings')
        print(mainBrain.raw_data[0])
        for heading in mainBrain.raw_data[0]:
            self.tree.heading(heading, text=heading)
            self.tree.column(heading, width = 50)
        self.tree.column(mainBrain.raw_data[0][0], width = 100)
    
    def open_choice_window(self):
        self.choiceWindow = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
        self.choiceWindow.title("Particle Simulation")
        self.choiceWindow.geometry("800x450")

        self.write_tree_headings()
        self.write_experiments_to_tree()

        #self.tree.grid(row=0, column=0, sticky='nsew')


        scrollbar = ttk.Scrollbar(self.choiceWindow, orient=tkinter.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(fill="y")
        self.tree.pack(fill="x")

        start_button = tkinter.Button(self.choiceWindow, text = "Start!", width = 10, height = 5, command = self.selected_experiment, background="grey")
        start_button.pack(fill="x")

        self.choiceWindow.mainloop()




