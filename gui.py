import tkinter
from tkinter import ttk

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
    
    def selected_experiment(self):
        print(self.tree.selection()[0])
    
    def open_choice_window(self):
        from Brain import mainBrain
        self.choiceWindow = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
        self.choiceWindow.title("Particle Simulation")
        self.choiceWindow.geometry("800x450")

        column = ("experimentName")
        print("columns =",column)

        self.tree = ttk.Treeview(self.choiceWindow, columns=column, show='headings')
        self.tree.heading('experimentName', text='Experiment Name')
        i = 0
        for experiment in mainBrain.particle_list:
            self.tree.insert('', tkinter.END, values=(experiment.name, ),iid={i})
            i+=1

        self.tree.grid(row=0, column=0, sticky='nsew')


        scrollbar = ttk.Scrollbar(self.choiceWindow, orient=tkinter.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        start_button = tkinter.Button(self.choiceWindow, text = "Start!", width = 10, height = 5, command = self.selected_experiment, background="grey")
        start_button.grid(row=0,column=1)

        self.choiceWindow.mainloop()




