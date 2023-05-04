from ParticleSim import SimBrain as Brain
import unittest


class BrainTestCase(unittest.TestCase):
    testDataPath = "cfmTestSpreadsheet.csv"

    def setUp(self):
        self.pyBrain = Brain.mainBrain

    def test_OpenData(self):
        self.assertEqual(
            type(self.pyBrain.open_csv(self.testDataPath)), list, "Import data failed"
        )
        self.assertEqual(
            type(
                self.pyBrain.import_experiments(
                    self.pyBrain.open_csv(self.testDataPath)
                )
            ),
            list[self.pyBrain.ParticleSimulation],
            "Failed to translate data",
        )

    def test_translateReadData(self):
        self.assertEqual(
            type(self.pyBrain.loadDataFromPath(self.testDataPath)),
            list[self.pyBrain.ParticleSimulation],
            "ReadData of wrong type",
        )

    def test_calculation(self):
        data = self.pyBrain.ParticleSimulation(
            "TestParticle", 0, 5, 5, 45, 1, 0.5, 0.2, 1.28, 9.81
        )
        self.assertEqual(
            type(self.pyBrain.calculateFor(data)) == True
        ), "Failed to calculate experiment"
