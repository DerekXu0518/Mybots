import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    
    def __init__(self, jointName):
        self.jointName = jointName

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50)
    
    def Save_Values(self):
        numpy.save("data/motorValues", self.motorValues)