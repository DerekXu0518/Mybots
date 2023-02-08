import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c


class SOLUTION:

	def __init__(self, nextAvailableID):

		self.lastI = random.randint(2,10)

		self.numMotorNeuron = self.lastI-1

		#self.weights = numpy.random.rand(self.numSensor,self.numMotorNeuron) * 2 - 1

		self.myID = nextAvailableID

		self.sensors = {}

		self.motors = {}

		self.neuronId = 0

		self.numSensor = 0

	def Start_Simulation(self, directOrGUI):

		if self.myID == 0:

			self.Create_World()

		self.Generate_Body()

		print("This is start of generate brain")

		self.Generate_Brain()

		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID)+" 2&>1 &")

	def Wait_For_Simulation_To_End(self):

		while not os.path.exists("Fitness" + str(self.myID) + ".txt"):

			time.sleep(0.01)

		f = open("Fitness" + str(self.myID) + ".txt", 'r')

		self.overallFitness = f.readlines()

		f.close()

		self.xfitness = float(self.overallFitness[0])

		self.yfitness = float(self.overallFitness[1])

		os.system("rm Fitness" + str(self.myID) + ".txt")

	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		pyrosim.End()

	def Generate_Body(self):

		pyrosim.Start_URDF("body"+str(self.myID)+".urdf")

		for i in range(1,self.lastI+1):

			if random.random() <0.5:

				self.material = "Green"

				self.color = "0 1.2 0 1.0"

				self.numSensor +=1

			else:

				self.material = "Blue"

				self.color = "0 0 2.5 1.0"

			randomX = random.uniform(0,1)

			randomY = random.uniform(0,1)

			randomZ = random.uniform(0,1)

			if i == 1:

				pyrosim.Send_Cube(name="Torso1", pos=[0, 0, 2], size=[randomX, randomY, randomZ],
									  materialName=self.material,colorRgba=self.color)

				if self.material == 'Green':# generate a neuron

					self.sensors[i] = "Torso1"

				pyrosim.Send_Joint(name="Torso1_Torso2", parent="Torso1", child="Torso2", type="revolute",
									   position=[randomX / 2, 0, 2], jointAxis="0 1 0")

				self.motors[i] = "Torso1_Torso2"

			elif i == self.lastI:

				pyrosim.Send_Cube(name="Torso" + str(i), pos=[randomX / 2, 0, 0], size=[randomX, randomY, randomZ],
									  materialName=self.material,colorRgba=self.color)

				if self.material == "Green": # generate a neuron

					self.sensors[i] = "Torso"+str(i)

			else:

				pyrosim.Send_Cube(name="Torso" + str(i), pos=[randomX / 2, 0, 0], size=[randomX, randomY, randomZ]
								  ,materialName=self.material, colorRgba=self.color)

				if self.material == "Green":# generate a neuron

					self.sensors[i] = "Torso"+str(i)

				pyrosim.Send_Joint(name="Torso"+str(i)+"_Torso"+str(i+1), parent="Torso"+str(i), child="Torso"+str(i+1), type="revolute",
								   position=[randomX, 0, 0], jointAxis="0 1 0")

				self.motors[i] = "Torso"+str(i)+"_Torso"+str(i+1)

		pyrosim.End()

	def Generate_Brain(self):

		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

		print(self.sensors)

		for i in self.sensors.keys():

			pyrosim.Send_Sensor_Neuron(name=self.neuronId, linkName=self.sensors[i])

			self.neuronId +=1

		for i in self.motors.keys():

			pyrosim.Send_Motor_Neuron(name=self.neuronId, jointName=self.motors[i])

			self.neuronId +=1

		self.weights = numpy.random.rand(self.numSensor, self.numMotorNeuron) * 2 - 1

		for currentRow in range(self.numSensor):

			for currentColumn in range(self.numMotorNeuron):

				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+self.numSensor, weight=self.weights[currentRow][currentColumn])

		pyrosim.End()

		self.neuronId = 0

		self.numSensor = 0

		self.sensors = {}

	def Mutate(self):

		randomRow = random.randint(0,len(self.weights) -1)

		randomColumn = random.randint(0,len(self.weights[0]) -1)

		self.weights[randomRow, randomColumn] = random.random()*2-1

	def Set_ID(self, ID):

		self.myID = ID




