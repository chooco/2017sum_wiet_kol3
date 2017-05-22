#source_katarzynaadr

import unittest, math
from simulation import Plane, Simulation


class Mock(object):
    def __init__(self):
        self.was_called = False

    def __call__(self, *args, **kwargs):
        self.was_called = True


class TestPlaneTask(unittest.TestCase):
    def test_angle_test(self):
        plane = Plane(0)
        self.assertEqual(plane.angle, 0)

        plane = Plane(16)
        self.assertEqual(plane.angle, 16)

    def test_angle_test_default(self):
        plane = Plane(0)
        self.assertEqual(plane.angle, 0)

    def test_letters_angle_test(self):
        plane = Plane('bcd')
        self.assertEqual(plane.angle, 'bcd')

    def test_square_angle_test(self):
        plane = Plane(math.sqrt(16))
        self.assertEqual(plane.angle, math.sqrt(16))


    def test_complex_angle_test(self):
        plane = Plane(15j)
        self.assertEqual(plane.angle, 15j)

    def test_negative_complex_test(self):
        plane = Plane(-15j)
        self.assertEqual(plane.angle, -15j)


    def test_test_adjust_tilt(self):
        plane = Plane(73)
        self.assertEqual(plane.angle, 73)

    def test_negative_angle_test(self):
        plane = Plane(-30)
        plane.correct_tilt()
        self.assertEqual(plane.angle, 0)

    def test_non_float_angle_test(self):
        plane = Plane(5.4)
        plane.correct_tilt()
        self.assertEqual(plane.angle, 0.0)

    def test_negative_non_float_angle_test(self):
        plane = Plane(-5.4)
        plane.correct_tilt()
        self.assertEqual(plane.angle, 0.0)




class TestSimulationTask(unittest.TestCase):


    def test_simulate_correct_test(self):
        plane = Plane(0)
        plane.correct_tilt = Mock()
        self.assertTrue(plane.correct_tilt)

    def test_simulate_generate_test(self):
        plane = Plane(0)
        plane.generate_tilt = Mock()
        self.assertTrue(plane.generate_tilt)



if __name__ == '__main__':
    unittest.main()
