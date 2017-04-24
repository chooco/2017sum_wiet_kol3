#source_katarzynaadr

import unittest
from simulation import Plane, Simulation


class Mock(object):
    def __init__(self):
        self.was_called = False

    def __call__(self, *args, **kwargs):
        self.was_called = True

class testPlaneTask(unittest.TestCase):
    simulate = Simulation()
    plane = Plane()

    def correct_tilt_test(self):
        plane = Plane(53)
        plane.adjust_tilt()
        self.assertEqual(plane.angle, 0)

    def angle_test(self):
        plane = Plane(5)
        self.assertEqual(plane.angle, 5)

class testSimulationTask(unittest.TestCase):
    simulate = Simulation()
    plane = Plane()

    def simulate_test(self):
        plane = Plane(0)
        simulation = Simulation(Plane)
        self.assertIs(simulation.plane, plane)

    def simulate_correct_test(self):
        plane = Plane(0)
        plane.correct_tilt = Mock()
        self.assertTrue(plane.correct_tilt)


    def simulate_generate_test(self):
        plane = Plane(0)
        plane.generate_tilt = Mock()
        self.assertTrue(plane.generate_tilt)

    def next_step_test(self):
        self.assertEqual(next(self.simulation))

    def end_of_simulation_test(self):
        plane = Plane(0)
        simulation = Simulation(plane)
        self.assertIsNone(simulation.end_of_simulation())
        self.assertEqual("End of simulation")

