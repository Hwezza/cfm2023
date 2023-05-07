from SimBrain import SimBrain as Brain
import unittest


class BrainTestCase(unittest.TestCase):
    testDataPath = "cfmTestSpreadsheet.csv"
    pyBrain: Brain

    def setUp(self):
        self.pyBrain = Brain()

    def test_getData(self):
        test_brain = Brain()
        data = test_brain.ParticleSimulation(
            'Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81)
        test_brain.particle_list = [data]
        self.assertEqual(test_brain.particle_list[0].getData(), ['Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81, 'N/A', 'N/A', 'N/A', 'N/A'], 'getData() failed')
    
    def test_updateResults(self):
        test_brain = Brain()
        data = test_brain.ParticleSimulation(
            'Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81)
        test_brain.particle_list = [data]
        test_brain.particle_list[0].updateResults("It", "is", "all", "good")
        [self.assertIn(i, test_brain.particle_list[0].getData(), 'Failed to update results') for i in ["It", "is", "all", "good"]]
    
    def test_OpenData(self):
        data1 = self.pyBrain.open_csv(self.testDataPath)
        self.assertEqual(type(data1), list, "data not importing as list")
        
        self.pyBrain.particle_list = []
        self.pyBrain.import_experiments(self.pyBrain.open_csv(path=self.testDataPath))
        self.assertEqual(self.pyBrain.particle_list[0].getData(), ['Example1', 18.9, 15.8, 17.2, 1.11, 14.5, 27.2, 1.6, 10.4, 9.98, 'N/A', 'N/A', 'N/A', 'N/A'], 'imported data incorrect')

    def test_translateReadData(self):
        self.assertEqual(
            self.pyBrain.openDataFromPath(self.testDataPath),
            self.pyBrain.particle_list,
            "ReadData of wrong type",
        )

    def test_example(self):
        test_brain = Brain()
        data = test_brain.ParticleSimulation(
            'Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81)
        test_brain.particle_list = [data]
        result = test_brain.calculateFor(0)
        x = result[1][0]
        z = result[1][2]
        test_brain.particle_list[0].updateResults(
            dx=x[-1],
            tx=result[0].t_events[0][0],
            dz=max(z),
            tz=result[0].t_events[1][0],
        )
        self.assertEqual((x[-1], result[0].t_events[0][0],
                          max(z), result[0].t_events[1][0]), (1.922734288944554, 0.6911539995997071, 0.6129504928799111, 0.2901047059396015), "failed test calculation")

    def test_update_data(self):
        test_brain = Brain()
        data = test_brain.ParticleSimulation(
            'Our_Particle', 10, 8, 6, 0.52, 5, 2, 1.2, 5.6, 9.81)
        test_brain.particle_list = [data]

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(BrainTestCase)
    unittest.TextTestRunner().run(suite)
