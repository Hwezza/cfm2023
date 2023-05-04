# Main File
from SimBrain import SimBrain
from gui import guibrain

pyBrain = SimBrain()
guibrain.mainBrain = pyBrain
path = 'cfmTestSpreadsheet.csv'

# startup
pyBrain.openDataFromPath(path)

# Menu
guibrain.open_menu()
