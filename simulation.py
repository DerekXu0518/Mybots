import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT


class SIMULATION:
    # see computer conditions


    def __init__(self, directOrGUI):
        physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)
        #if directOrGUI == 'DIRECT':
           # p.connect(p.DIRECT)
        #else:
           # p.connect(p.GUI)
        self.world = WORLD()
        self.robot = ROBOT()


    def Run(self):
        for t in range(0, 1000):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act(t)
            time.sleep(1 / 300)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()


