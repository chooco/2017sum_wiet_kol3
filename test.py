#source_katarzynaadr

import unittest, math
from simulation import Plane, Simulation


class Mock(object):
    def __init__(self):
        self.was_called = False

    def __call__(self, *args, **kwargs):
        self.was_called = True

class SysStdOut(object):
    def __init__(self):
        self.history = []

    def write(self, msg):
        self.history.append(msg)

class TestPlaneTask(unittest.TestCase):
    def angle_test(self):
        plane = Plane(0)
        self.assertEqual(plane.angle, 0)

        plane = Plane(16)
        self.assertEqual(plane.angle, 16)

    def angle_test_default(self):
        plane = Plane()
        self.assertEqual(plane.angle, 0)

    def letters_angle_test(self):
        plane = Plane('bcd')
        self.assertEqual(plane.angle, 0)

    def square_angle_test(self):
        x=sqrt(27)
        plane = Plane('x')
        self.assertEqual(plane.angle, x)


    def complex_angle_test(self):
        plane = Plane(15j)
        self.assertEqual(plane.angle, 0)

    def negative_complex_test(self):
        plane = Plane(-15j)
        self.assertEqual(plane.angle, 0)


    def test_adjust_tilt(self):
        plane = Plane(73)
        self.assertEqual(plane.angle, 73)

    def negative_angle_test(self):
        plane = Plane(-30)
        plane.adjust_tilt()
        self.assertEqual(plane.angle, 0)

    def non_float_angle_test(self):
        plane = Plane(5.4)
        plane.adjust_tilt()
        self.assertEqual(plane.angle, 0.0)

    def negative_non_float_angle_test(self):
        plane = Plane(-5.4)
        plane.adjust_tilt()
        self.assertEqual(plane.angle, 0.0)




class TestSimulationTask(unittest.TestCase):


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

    def end_of_simulation_test(self):
        plane = Plane(0)
        simulation = Simulation(plane)
        self.assertIsNone(simulation.end_of_simulation())
        self.assertEqual("End of simulation")

if __name__ == '__main__':
    unittest.main()
