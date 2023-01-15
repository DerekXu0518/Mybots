import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.backLegAmplitude
        self.frequency = c.backLegFrequency
        self.offset = c.backLegPhaseOffset
        self.X = numpy.linspace(self.offset, 2 * self.frequency * numpy.pi + self.offset, 1000)
        self.motorValues = numpy.sin(self.X) * self.amplitude

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=60)
