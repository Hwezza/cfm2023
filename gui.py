import tkinter as Tk
### Main window
def open_menu():
    main_window = Tk.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    main_window.title("Home")
    main_window.geometry("800x450")

    # choices:
    first_option = Tk.Button(main_window, text = "Particle Catapult", width = 10, height = 5, command = open_program1)
    first_option.place(x=20,y=20)
    first_label = Tk.Label(main_window, text= "Particle catapult:\n ???",
                                width = 60, height = 5, background= "grey")
    first_label.place(x=180, y=20)
    main_window.mainloop()


### Program 1 (particleSim)
def open_program1():
    program1_window = Tk.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    program1_window.title("Particle Catapult")
    program1_window.geometry("800x450")
    
    program1_window.mainloop()





