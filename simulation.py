import time
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        # see computer conditions
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.8)

        self.world = WORLD()
        self.robot = ROBOT()
        pyrosim.Prepare_To_Simulate(self.robot.robotId)
        ROBOT.Prepare_To_Sense(self.robot.robotId)

    def Run(self):
        for i in range(0, 1000):
            print(i)
            p.stepSimulation()
# retrieve sensorValues
#   backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
#  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
# backLeg joint motor
# pyrosim.Set_Motor_For_Joint(
#    bodyIndex=robotId,
#   jointName=b"Torso_BackLeg",
#  controlMode=p.POSITION_CONTROL,
# targetPosition=backLegTargetAngles[i],
# maxForce=60)
# frontLeg joint motor
# pyrosim.Set_Motor_For_Joint(
#    bodyIndex=robotId,
#   jointName=b"Torso_FrontLeg",
#  controlMode=p.POSITION_CONTROL,
# targetPosition=frontLegTargetAngles[i],
# maxForce=60)
            time.sleep(1 / 60)
    def __del__(self):
        p.disconnect()


