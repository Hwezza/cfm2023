from Brain import mainBrain as pyBrain

testDataPath = "cfmTestSpreadsheet.csv"


def test_OpenData():
    assert type(pyBrain.open_csv(testDataPath)) == list, "Import data failed"
    assert (
        type(pyBrain.import_experiments(pyBrain.open_csv(testDataPath)))
        == list[pyBrain.ParticleSimulation]
    ), "Failed to translate data"


def test_translateReadData():
    assert (
        type(pyBrain.loadDataFromPath(testDataPath)) == list[pyBrain.ParticleSimulation]
    ), "ReadData of wrong type"


def test_calculation():
    data = pyBrain.ParticleSimulation(
        "TestParticle", 0, 5, 5, 45, 1, 0.5, 0.2, 1.28, 9.81
    )
    assert type(pyBrain.calculateFor(data)) == True, "Failed to calculate experiment"

