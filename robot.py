import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c
import math


class ROBOT:
    def __init__(self, solutionID):
        self.sensors = {}
        self.motors = {}
        self.solutionID = solutionID
        self.robotId = p.loadURDF("body"+self.solutionID+".urdf")
        self.nn = NEURAL_NETWORK("brain"+self.solutionID+".nndf")
        os.system("rm brain" + self.solutionID + ".nndf")
        os.system("rm body" + self.solutionID + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors:
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
                self.motors[jointName].Set_Value( self.robotId, desiredAngle)
                #print(neuronName, jointName, desiredAngle)

    def Think(self):
        self.nn.Update()
        #self.nn.Print()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]
        yPosition = basePosition[1]
        distance = yPosition
        f=open("temp"+self.solutionID+".txt", 'w')
        rewrite = "mv temp"+str(self.solutionID)+".txt Fitness" + str(self.solutionID)+".txt"
        os.system(rewrite)
        #f.write(str(xPosition))
        #f.write(str(xPosition) + "\n" + str(yPosition) + "\n")
        f.write(str(distance))
        f.close()
        #print(xCoordinateOfLinkZero)
