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

		f.close()

		self.xfitness = float(self.overallFitness[0])

		self.yfitness = float(self.overallFitness[1])

		os.system("rm Fitness" + str(self.myID) + ".txt")

	def Create_World(self):

		pyrosim.Start_SDF("world.sdf")

		#pyrosim.Send_Sphere(name="BowlingBall", pos=[-3, +3, 0.5], size=[0.5])

		#pyrosim.Send_Cube(name="Stair1", pos=[1, 0, 1], size=[2, 3.5, 2],mass=100.0)

		#pyrosim.Send_Cube(name="Stair2", pos=[-0.5, 0, 0.9], size=[1, 3.5, 1.8], mass=100.0)

		#pyrosim.Send_Cube(name="Stair3", pos=[-1.5, 0, 0.8], size=[1, 3.5, 1.6], mass=100.0)

		#pyrosim.Send_Cube(name="Stair4", pos=[-2.5, 0, 0.7], size=[1, 3.5, 1.4], mass=100.0)

		#pyrosim.Send_Cube(name="Stair5", pos=[-3.5, 0, 0.6], size=[1, 3.5, 1.2], mass=100.0)

		pyrosim.End()

	def Generate_Body(self):

		pyrosim.Start_URDF("body.urdf")

		# First Link

		firstX = random.uniform(0, 1)

		firstY = random.uniform(0, 1)

		firstZ = random.uniform(0, 1)

		pyrosim.Send_Cube(name="Torso1", pos=[0, 0, 3], size=[firstX,firstY,firstZ], materialName="Green", colorRgba="0 1.28 0 1.0")

		pyrosim.Send_Joint(name="Torso1_Torso2", parent="Torso1", child="Torso2", type="revolute",position=[firstX / 2, 0, 3], jointAxis="0 1 0")

		for i in range(2,random.randint(3,10)):

			randomX = random.uniform(0,1)

			randomY = random.uniform(0,1)

			randomZ = random.uniform(0,1)

			if  random.choice([0,1]) == 0: # no sensor

				pyrosim.Send_Cube(name="Torso"+str(i), pos=[randomX/2, 0, 0], size=[randomX,randomY,randomZ],materialName="Blue",colorRgba="0 0 2.55 1.0")

			else: # with sensor

				pyrosim.Send_Cube(name="Torso" + str(i), pos=[randomX / 2, 0, 0], size=[randomX, randomY, randomZ],materialName="Green", colorRgba="0 1.28 0 1.0")

			pyrosim.Send_Joint(name="Torso0"+str(i)+"_Torso"+str(i+1), parent="Torso"+str(i), child="Torso"+str(i+1), type="revolute", position=[randomX, 0, 0], jointAxis="0 1 0")

		# Last Link

		lastX = random.uniform(0, 1)

		lastY = random.uniform(0, 1)

		lastZ = random.uniform(0, 1)

		pyrosim.Send_Cube(name="Torso" + str(i+1), pos=[lastX/2, 0, 0], size=[lastX,lastY,lastZ])

		pyrosim.End()

	def Generate_Brain(self):

		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

		pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso1")

		pyrosim.Send_Motor_Neuron(name=1, jointName="Torso1_Torso2")

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




