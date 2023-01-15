# import necessary conditions
#import random
#import pybullet as p
#import time
#import pybullet_data
#import pyrosim.pyrosim as pyrosim
#import numpy
#import constants as c
from simulation import SIMULATION


#backLegX = numpy.linspace(c.backLegPhaseOffset, 2*c.backLegFrequency*numpy.pi+c.backLegPhaseOffset, 1000)
#backLegTargetAngles = numpy.sin(backLegX)*c.backLegAmplitude
#frontLegX = numpy.linspace(c.frontLegPhaseOffset, 2*c.frontLegFrequency*numpy.pi+c.frontLegPhaseOffset, 1000)
#frontLegTargetAngles = numpy.sin(frontLegX)*c.frontLegAmplitude
#numpy.save("data/backLegTargetAngles", backLegTargetAngles)
#numpy.save("data/frontLegTargetAngles", frontLegTargetAngles)

# see computer conditions
#physicsClient = p.connect(p.GUI)
#p.setAdditionalSearchPath(pybullet_data.getDataPath())

#p.setGravity(0, 0, -9.8)

# create a world for robot
#planeId = p.loadURDF("plane.urdf")
#robotId = p.loadURDF("body.urdf")
#p.loadSDF("world.sdf")
#pyrosim.Prepare_To_Simulate(robotId)

# set front and backLeg values to zero
#backLegSensorValues = numpy.zeros(1000)
#frontLegSensorValues = numpy.zeros(1000)

# the main iteration
#for i in range(0, 1000):
 #   p.stepSimulation()
    # retrieve sensorValues
 #   backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  #  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    # backLeg joint motor
   # pyrosim.Set_Motor_For_Joint(
    #    bodyIndex=robotId,
     #   jointName=b"Torso_BackLeg",
      #  controlMode=p.POSITION_CONTROL,
       # targetPosition=backLegTargetAngles[i],
        #maxForce=60)
    # frontLeg joint motor
   # pyrosim.Set_Motor_For_Joint(
    #    bodyIndex=robotId,
     #   jointName=b"Torso_FrontLeg",
      #  controlMode=p.POSITION_CONTROL,
       # targetPosition=frontLegTargetAngles[i],
        #maxForce=60)
    #time.sleep(1 / 2400)

#p.disconnect()

# save values to .npy file
#numpy.save("data/backLegSensorValues", backLegSensorValues)
#numpy.save("data/frontLegSensorValues", frontLegSensorValues)

simulation = SIMULATION()
simulation.Run()




