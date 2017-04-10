import time

from simulation import Plane, Simulation


if __name__ == "__main__":
    angle = float(raw_input("Enter current angle\n"))
    plane = Plane(angle)
    simulation = Simulation(plane)
    
    while True:
        try:
            simulation.next_step()
            time.sleep(2)
        except KeyboardInterrupt:
            simulation.end_of_simulation()
            break