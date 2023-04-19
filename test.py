### test file
import sys
from sys import platform
if platform == "darwin":
    # OS X
    sys.path.insert(1, 'macLib')
elif platform == "win32":
    # Windows
    sys.path.insert(1, 'winLib')


def refreshData():
    # create example data in the test spreadsheet
    # this fills cfmTestSpreadsheet with random floats  within a specified range


    import csv
    from numpy import pi
    import random
    from random import randint
    columns = ("name","u","x","z","angle",'mass','diam','air res','air dens','grav')
    with open('cfmTestSpreadsheet.csv', 'w') as test_file:
        writer = csv.writer(test_file)
        writer.writerow(columns)
        for i in range(1,21):
            name = "Example"+str(i)
            u = randint(1,200)/10
            x = randint(1,200)/10
            z = randint(1,200)/10
            angle = round(random.uniform(0, pi/2), 2)
            mass = randint(1,200)/10
            diam = randint(1,300)/10
            air_res = randint(1,300)/10
            air_dens = randint(1,200)/10
            grav = randint(10,1000)/100
            writer.writerow((name, u, x, z, angle, mass, diam, air_res, air_dens, grav))



