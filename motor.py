import pybullet as p
import numpy
import pyrosim.pyrosim as pyrosim
import constants as c


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        #self.Prepare_To_Act()

    #def Prepare_To_Act(self):
        #set parameters for target angle, back leg is half frequency of front leg
        #if self.jointName == b'Torso_BackLeg':
         #   self.frequency = c.Frequency * 1 / 2
       # else:
        #    self.frequency = c.Frequency
        #self.amplitude = c.Amplitude
        #self.offset = c.Offset
        #self.X = numpy.linspace(self.offset, 2 * self.frequency * numpy.pi + self.offset, 1000)
        #self.motorValues = numpy.sin(self.X) * self.amplitude

    def Set_Value(self, robotId, desiredAngle):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 50) 
    
    def Save_Values(self):
        numpy.save("data/motorValues", self.motorValues)