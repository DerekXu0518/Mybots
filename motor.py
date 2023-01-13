import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()


    def Prepare_To_Act(self, amplitude, frequency, offset):
        self.amplitude = amplitude
        self.frequency = frequency
        self.offset = offset
        amplitude = 0.8
        frequency = 10
        offset = 0
        self.X = numpy.linspace(self.offset, 2 * self.frequency * numpy.pi + self.offset, 1000)
        self.motorValues = numpy.sin(self.X) * self.amplitude


    def Set_Value(self, t):
            pyrosim.Set_Motor_For_Joint(
            bodyIndex=self.robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=60)
