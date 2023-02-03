import tkinter
### Main window
def open_menu():
    main_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    main_window.geometry("800x450")

    # choices:
    first_option = tkinter.Button(main_window, text = "Option 1", width = 10, height = 5, command = open_program1)
    first_option.place(x=20,y=20)

    main_window.mainloop()


### Program 1 (Volumes of revolution?)
def open_program1():
    program1_window = tkinter.Tk(screenName=None,  baseName=None,  className='Window',  useTk=1)
    program1_window.geometry("800x450")
    
    program1_window.mainloop()




