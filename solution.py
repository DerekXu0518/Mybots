import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c


class SOLUTION:

	def __init__(self, nextAvailableID):

		self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1

		self.myID = nextAvailableID

	def Start_Simulation(self, directOrGUI):

		if self.myID == 0:

			self.Create_World()

			self.Generate_Body()

		self.Generate_Brain()

		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID)+" 2&>1 &")

	def Wait_For_Simulation_To_End(self):

		while not os.path.exists("Fitness" + str(self.myID) + ".txt"):

			time.sleep(0.1)

		f = open("Fitness" + str(self.myID) + ".txt", 'r')

		self.overallFitness = f.readlines()

		self.xfitness = float(self.overallFitness[0])

		self.yfitness = float(self.overallFitness[1])

		f.close()

		os.system("rm Fitness" + str(self.myID) + ".txt")

	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		pyrosim.Send_Cube(name="Box", pos=[-5, 0, 0.5], size=[20, 3.5, 1])

		pyrosim.End()

	def Generate_Body(self):

		pyrosim.Start_URDF("body.urdf")

		pyrosim.Send_Cube(name="Torso", pos=[0, 0, 2], size=[1, 1, 1])

		# Frist pair

		pyrosim.Send_Joint(name="Torso_LeftLeg1", parent="Torso", child="LeftLeg1", type="revolute", position=[-0.5, -0.5, 2], jointAxis="0 0 1")

		pyrosim.Send_Cube(name="LeftLeg1", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

		pyrosim.Send_Joint(name="Torso_RightLeg1", parent="Torso", child="RightLeg1", type="revolute", position=[-0.5, 0.5, 2], jointAxis="0 0 1")

		pyrosim.Send_Cube(name="RightLeg1", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

		pyrosim.Send_Joint(name="LeftLeg1_LeftLowerLeg1", parent="LeftLeg1", child="LeftLowerLeg1", type="revolute", position=[0, -1, 0], jointAxis="0 1 0")

		pyrosim.Send_Cube(name="LeftLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

		pyrosim.Send_Joint(name="RightLeg1_RightLowerLeg1", parent="RightLeg1", child="RightLowerLeg1", type="revolute", position=[0, 1, 0], jointAxis="0 1 0")

		pyrosim.Send_Cube(name="RightLowerLeg1", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

		# Second pair

		pyrosim.Send_Joint(name="Torso_LeftLeg2", parent="Torso", child="LeftLeg2", type="revolute", position=[0.5, -0.5, 2], jointAxis="1 0 0 ")

		pyrosim.Send_Cube(name="LeftLeg2", pos=[0, -0.5, 0], size=[0.2, 1, 0.2])

		pyrosim.Send_Joint(name="Torso_RightLeg2", parent="Torso", child="RightLeg2", type="revolute", position=[0.5, 0.5, 2], jointAxis="1 0 0")

		pyrosim.Send_Cube(name="RightLeg2", pos=[0, 0.5, 0], size=[0.2, 1, 0.2])

		pyrosim.Send_Joint(name="LeftLeg2_LeftLowerLeg2", parent="LeftLeg2", child="LeftLowerLeg2", type="revolute", position=[0, -1, 0], jointAxis="1 0 0")

		pyrosim.Send_Cube(name="LeftLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

		pyrosim.Send_Joint(name="RightLeg2_RightLowerLeg2", parent="RightLeg2", child="RightLowerLeg2", type="revolute", position=[0, 1, 0], jointAxis="1 0 0")

		pyrosim.Send_Cube(name="RightLowerLeg2", pos=[0, 0, -0.5], size=[0.2, 0.2, 1])

		pyrosim.End()

	def Generate_Brain(self):

		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

		pyrosim.Send_Sensor_Neuron(name=0, linkName="LeftLowerLeg1")

		pyrosim.Send_Sensor_Neuron(name=1, linkName="RightLowerLeg1")

		pyrosim.Send_Sensor_Neuron(name=2, linkName="LeftLowerLeg2")

		pyrosim.Send_Sensor_Neuron(name=3, linkName="RightLowerLeg2")

		pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_LeftLeg1")

		pyrosim.Send_Motor_Neuron(name=5, jointName="Torso_RightLeg1")

		pyrosim.Send_Motor_Neuron(name=6, jointName="LeftLeg1_LeftLowerLeg1")

		pyrosim.Send_Motor_Neuron(name=7, jointName="RightLeg1_RightLowerLeg1")

		pyrosim.Send_Motor_Neuron(name=8, jointName="Torso_LeftLeg2")

		pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_RightLeg2")

		pyrosim.Send_Motor_Neuron(name=10, jointName="LeftLeg2_LeftLowerLeg2")

		pyrosim.Send_Motor_Neuron(name=11, jointName="RightLeg2_RightLowerLeg2")

		for currentRow in range(c.numSensorNeurons):

			for currentColumn in range(c.numMotorNeurons):

				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+c.numSensorNeurons, weight=self.weights[currentRow][currentColumn])

		pyrosim.End()

	def Mutate(self):

		randomRow = random.randint(0,len(self.weights) -1)

		randomColumn = random.randint(0,len(self.weights[0]) -1)

		self.weights[randomRow, randomColumn] = random.random()*2-1

	def Set_ID(self, ID):

		self.myID = ID




