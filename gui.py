import tkinter
### Main window
def open_menu():
    main_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    main_window.title("Home")
    main_window.geometry("800x450")

    # choices:
    first_option = tkinter.Button(main_window, text = "Volumes of\nRevolution", width = 10, height = 5, command = open_program1)
    first_option.place(x=20,y=20)
    first_label = tkinter.Label(main_window, text= "Volumes of Revolution:\n Mapping the area of the 3D figure created by wrapping a 2D graph around the y (or x) axis.",
                                width = 60, height = 5, background= "grey")
    first_label.place(x=180, y=20)
    main_window.mainloop()


### Program 1 (Volumes of revolution?)
def open_program1():
    program1_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    program1_window.title("Volumes of Revolution")
    program1_window.geometry("800x450")
    
    program1_window.mainloop()




