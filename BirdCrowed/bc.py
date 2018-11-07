import math
import numpy as np

# 计算类鸟群的位置和速度
width, height = 640, 480


class Biods:
    """class that represents Boids simulation"""
    def __init__(self, N):
        """initialize the Boid simulation"""
        self.pos = [width/2.0, height/2.0] + 10 * np.random.rand(2*N).reshape(N, 2)
        # normalized random velocities
        angles = 2*math.pi*np.random.rand(N)
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.N = N
        # minimum distance of approach
        self.minDist = 25.0
        # maximum magnitude of velocities calculated by "rules"
        self.maxRuleVel = 0.03
        # maximum maginitude of the final velocity
        self.maxVel = 2.0

    def tick(self, frameNum, pts, beak):
        """update the simulation by one time step"""
        # get pairwise distances
        self.distMatris = sq
