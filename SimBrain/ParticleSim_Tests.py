from ParticleSim import SimBrain as Brain
import unittest


class BrainTestCase(unittest.TestCase):
    testDataPath = "cfmTestSpreadsheet.csv"
    pyBrain: Brain

    def setUp(self):
        self.pyBrain = Brain()

    def test_OpenData(self):
        self.assertEqual(
            type(self.pyBrain.open_csv(self.testDataPath)
                 ), list, "Import data failed"
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

    def test_example(self):
        test_brain = Brain()
        data = test_brain.ParticleSimulation(
            'Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81)
        test_brain.particle_list.append(data)
        result = test_brain.calculateFor(0)
        x = result[1][0]
        z = result[1][2]
        test_brain.particle_list[0].updateResults(
            dx=x[-1],
            tx=result[0].t_events[0][0],
            dz=max(z),
            tz=result[0].t_events[1][0],
        )
        print(x[-1], result[0].t_events[0][0],max(z),result[0].t_events[1][0])

our_test = BrainTestCase()
our_test.test_example()