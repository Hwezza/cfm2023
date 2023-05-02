# Main File
import pyBrain.Brain as Brain
from gui import guibrain

pyBrain = Brain.mainBrain
path = 'cfmTestSpreadsheet.csv'

# startup
pyBrain.openDataFromPath(path)

# Menu
guibrain.open_menu()
