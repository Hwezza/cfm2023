import gui
class PyBrain:
    running = True
    
    def menu(self):
        gui.open_menu()
    
    def option1_selected(self):
        print("open option1")
        gui.open_program1



#testing
'''
brain = PyBrain()
brain.menu()
'''