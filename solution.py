import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time


class SOLUTION:

	def __init__(self, nextAvailableID):

		self.weights = numpy.random.rand(3, 2) * 2 - 1

		self.myID = nextAvailableID

	def Start_Simulation(self, directOrGUI):

		if self.myID == 0:

			self.Create_World()

			self.Generate_Body()

		self.Generate_Brain()

		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID)+" &")

	def Wait_For_Simulation_To_End(self):

		while not os.path.exists("Fitness" + str(self.myID) + ".txt"):

			time.sleep(0.2)

		f = open("Fitness" + str(self.myID) + ".txt", 'r')

		self.fitness = float(f.read())

		#print(self.fitness)

		f.close()

		os.system("rm Fitness" + str(self.myID) + ".txt")

	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		pyrosim.Send_Cube(name="Box", pos=[-2, 2, 0.5], size=[1, 1, 1])

		pyrosim.End()

	def Generate_Body(self):

		pyrosim.Start_URDF("body.urdf")

		pyrosim.Send_Cube(name="Torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])

		pyrosim.Send_Joint(name="Torso_BackLeg", parent="Torso", child="BackLeg", type="revolute", position=[1, 0, 1])

		pyrosim.Send_Cube(name="BackLeg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])

		pyrosim.Send_Joint(name="Torso_FrontLeg", parent="Torso", child="FrontLeg", type="revolute", position=[2, 0, 1])

		pyrosim.Send_Cube(name="FrontLeg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

		pyrosim.End()

	def Generate_Brain(self):

		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

		pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")

		pyrosim.Send_Sensor_Neuron(name=1, linkName="BackLeg")

		pyrosim.Send_Sensor_Neuron(name=2, linkName="FrontLeg")

		pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_BackLeg")

		pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_FrontLeg")

		for currentRow in range(3):

			for currentColumn in range(2):

				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])

		pyrosim.End()

	def Mutate(self):

		randomRow = random.randint(0,len(self.weights) -1)

		randomColumn = random.randint(0,len(self.weights[0]) -1)

		self.weights[randomRow, randomColumn] = random.random()*2-1

	def Set_ID(self, ID):

		self.myID = ID




