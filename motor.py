import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        print(jointName)

    def Prepare_To_Act(self):
        #set parameters for target angle
        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.Frequency * 1 / 2
        else:
            self.frequency = c.Frequency
        self.amplitude = c.Amplitude
        self.offset = c.Offset
        self.X = numpy.linspace(self.offset, 2 * self.frequency * numpy.pi + self.offset, 1000)
        self.motorValues = numpy.sin(self.X) * self.amplitude

    def Set_Value(self, t, robotId):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robotId,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.motorValues[t],
            maxForce=60)
    
    def Save_Values(self):
        numpy.save("data/motorValues", self.motorValues)