### test file


def create_test_data():
    import csv
    from numpy import pi
    import random
    from random import randint
    def refreshTestData():
        columns = ("name","u","x","z","angle",'mass','diam','air res','air dens','grav')
        with open('cfmTestSpreadsheet.csv', 'w') as test_file:
            writer = csv.writer(test_file)
            writer.writerow(columns)
            for i in range(1,20):
                name = "Example"+str(i)
                u = randint(0,20)
                x = randint(0,20)
                z = randint(0,20)
                angle = round(random.uniform(0, pi/2), 2)
                mass = randint(0,20)
                diam = randint(0,30)
                air_res = randint(0,300)/100
                air_dens = randint(0,200)/100
                grav = randint(1,1000)/100
                writer.writerow((name, u, x, z, angle, mass, diam, air_res, air_dens, grav))


    import numpy as np
    import absorption


def test_MM():
    import gui
    guibrain = gui.guibrain()
    guibrain.open_menu()
    guibrain.mainwindow
    assert type(guibrain.main_window)==True , "good"

def test_all():
    return 0

"""
This tests all of the code in the Brain of the code
"""




