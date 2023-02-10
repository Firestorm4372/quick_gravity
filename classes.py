import numpy as np

class Solar_System:
    """
    Container class for all bodies
    """
    def __init__(self, 
                 size = (10,10)
                ) -> None:
        self.contents = []
        self.size = size
        self.G = 1.0
        self.dt = 0.001

    def add_body(self,
                 mass = 1,
                 pos = (0,0), 
                 vel = (0,0)
                ) -> None:
        body = Body(mass,pos,vel)
        self.contents.append(body)

    def update_bodies(self) -> None:
        # Zero off the accelerations
        for body in self.contents:
            body.acc = (0,0)

        for i, body1 in enumerate(self.contents):
            for j, body2 in enumerate(self.contents[i+1:]):
                R = body2.pos - body1.pos
                F = self.G * body1.mass * body2.mass / (np.linalg.norm(R)**2)
                # F_vec points from 1 to 2
                F_vec = F * (R / np.linalg.norm(R))

                # Sum in the accelerations
                body1.acc += F / body1.mass
                body2.acc += -F / body2.mass

        for body in self.contents:
            body.update_position(self.dt)

class Body:
    """
    Base class for all possible bodies
    """
    def __init__(self,
                 mass,
                 pos, 
                 vel
                ) -> None:
        self.mass = mass
        self.pos = np.array(pos, 'float64')
        self.vel = np.array(vel, 'float64')
        self.acc = np.zeros(2, 'float64')
    
    def update_position(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt
    
