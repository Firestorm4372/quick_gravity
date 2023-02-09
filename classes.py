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
        self.G = 1
        self.dt = 1

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
                R = np.subtract(body2.pos, body1.pos)
                F = self.G * body1.mass * body2.mass / (np.linalg.norm(R)^2)
                # F_vec points from 1 to 2
                F_vec = F * (R / np.linalg.norm)

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
                 mass = 1,
                 pos = (0,0), 
                 vel = (0,0)
                ) -> None:
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = (0,0)
    
    def update_position(self, dt):
        self.vel += self.acc * dt
        self.pos += self.vel * dt
    
