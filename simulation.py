import random


class Plane(object):
    def __init__(self, angle):
        self.angle = angle

    def correct_tilt(self):
        self.angle -= self.angle

    def generate_tilt(self):
        self.angle = random.gauss(0, 1)


class Simulation(object):
    def __init__(self, plane):
        self.plane = plane
        self.simulation = self.simulate()

    def simulate(self):
        while True:
            print "*" * 50
            message = "Current angle: {}\nCorrection needed: {}\n"
            print message.format(self.plane.angle, -self.plane.angle)
            self.plane.correct_tilt()
            print "Orientation after correction: {}\n".format(self.plane.angle)
            self.plane.generate_tilt()
            yield
            
    def next_step(self):
        return next(self.simulation)
        
    def end_of_simulation(self):
        print "End of simulation"