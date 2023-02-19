import numpy
import os
import pyrosim.pyrosim as pyrosim
import random
import time
import constants as c


class SOLUTION:

	def __init__(self, nextAvailableID):

		self.myID = nextAvailableID

		self.sensors = []

		self.motors = []

		self.neuronId = 0

		self.numSensorNeuron = 0

		#linklist
		self.linkNameList = []

		self.sizeList = []

		self.linkPositionList=[]

		self.materialList = []

		self.colorList = []

		# jointlist
		self.jointNameList = []

		self.jointPositionList = []

		self.jointAxisList = []

		#random.seed(0)

		#numpy.random.seed(0)

	def Start_Simulation(self, directOrGUI):

		if self.myID == 0:

			self.Create_World()

		self.Generate_Body()

		self.Generate_Brain()

		#2 & > 1

		os.system("python3 simulate.py " + directOrGUI + " " + str(self.myID)+" &")

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

		self.Generate_Body_List()

		self.Generate_Body_From_Body_List()
		print(self.linkNameList)
		print(self.linkPositionList)

		pyrosim.End()

	def Generate_Body_List(self):

		self.length = random.randint(2,10)

		for i in range(self.length+1):

			self.Set_Color()

			self.Random_Size()

			self.Random_Joint_Axis()

			if i == 0:

				self.pick_axis = "x axis"

				self.linkNameList.append("Torso" + str(i))

				self.linkPositionList.append([0,0,3])

				self.materialList.append(self.material)

				self.colorList.append(self.color)

				self.sizeList.append([self.randomX, self.randomY, self.randomZ])

				self.jointAxisList.append(self.jointAxis)

				self.jointNameList.append("Torso" + str(i) + "_Torso" + str(i + 1))

				self.Random_Joint_Position(i)

				self.jointPositionList.append([self.randomX/2,0,3])

				self.jointAxisList.append(self.jointAxis)

			elif i==self.length:

				self.Decide_Link_Position()

				self.linkNameList.append("Torso" + str(i))

				self.linkPositionList.append(self.linkPosition)

				self.materialList.append(self.material)

				self.colorList.append(self.color)

				self.sizeList.append([self.randomX, self.randomY, self.randomZ])

			else:

				self.Decide_Link_Position()

				self.linkNameList.append("Torso"+str(i))

				self.linkPositionList.append(self.linkPosition)

				self.materialList.append(self.material)

				self.colorList.append(self.color)

				self.sizeList.append([self.randomX,self.randomY,self.randomZ])

				self.jointAxisList.append(self.jointAxis)

				self.jointNameList.append("Torso"+str(i)+"_Torso"+str(i+1))

				self.Random_Joint_Position(i)

				self.jointPositionList.append(self.jointPosition)


	def Generate_Body_From_Body_List(self):

		for i in range(1,len(self.linkNameList)):

			pyrosim.Send_Cube(name=self.linkNameList[i], pos=self.linkPositionList[i], size=self.sizeList[i],
									  materialName=self.materialList[i],colorRgba=self.colorList[i])

			if self.materialList[i] == "Green": # generate a neuron

				self.sensors.append(self.linkNameList[i])

		for i in range(1,len(self.jointNameList)):

			pyrosim.Send_Joint(name=self.jointNameList[i], parent=self.linkNameList[i], child=self.linkNameList[i+1], type="revolute",
								   position=self.jointPositionList[i], jointAxis=self.jointAxisList[i])

			self.motors.append(self.jointNameList[i])

	def Generate_Brain(self):

		self.numMotorNeuron = len(self.motors)

		pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

		for i in range(len(self.sensors)):

			pyrosim.Send_Sensor_Neuron(name=self.neuronId, linkName=self.sensors[i])

			self.neuronId +=1

		for i in range(len(self.motors)):

			pyrosim.Send_Motor_Neuron(name=self.neuronId, jointName=self.motors[i])

			self.neuronId +=1

		self.weights = numpy.random.rand(self.numSensorNeuron, self.numMotorNeuron) * 2 - 1

		for currentRow in range(self.numSensorNeuron):

			for currentColumn in range(self.numMotorNeuron):

				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+self.numSensorNeuron, weight=self.weights[currentRow][currentColumn])

		self.neuronId = 0

		pyrosim.End()

	def Mutate(self):

		randomRow = random.randint(0,len(self.weights) -1)

		randomColumn = random.randint(0,len(self.weights[0]) -1)

		self.weights[randomRow, randomColumn] = random.random()*2-1

	def Set_ID(self, ID):

		self.myID = ID

	def Set_Color(self):

		if random.random() < 0.5:

			self.material = "Green"

			self.color = "0 1.2 0 1.0"

			self.numSensorNeuron += 1

		else:

			self.material = "Blue"

			self.color = "0 0 2.5 1.0"

	def Random_Size(self):

		self.randomX = random.uniform(0.2, 1)

		self.randomY = random.uniform(0.2, 1)

		self.randomZ = random.uniform(0.2, 1)

	def Random_Joint_Position(self,i):

		if self.linkPositionList[i][0] !=0:

			self.jointPosition = random.choice([[self.sizeList[i][0]/2,self.sizeList[i][1]/2,0],[self.sizeList[i][0]/2,0,self.sizeList[i][2]/2]])

			if self.jointPosition[1] !=0:

				self.pick_axis = "y axis"

			else:

				self.pick_axis = "z axis"

		elif self.linkPositionList[i][1] != 0:

			self.jointPosition = random.choice([[0, self.sizeList[i][1] / 2, self.sizeList[i][2] / 2],[self.sizeList[i][0]/2,self.sizeList[i][1]/2,0]])

			if self.jointPosition[0] !=0:

				self.pick_axis = "x axis"

			else:

				self.pick_axis = "z axis"

		else:

			self.jointPosition = random.choice([[self.sizeList[i][0]/2,0,self.sizeList[i][2]/2],[0,self.sizeList[i][1]/2,self.sizeList[i][2]/2]])

			if self.jointPosition[0] !=0:

				self.pick_axis = "x axis"

			else:

				self.pick_axis = "y axis"

	def Decide_Link_Position(self):

		if self.pick_axis =="x axis":

			self.linkPosition = [self.randomX/2,0,0]

		elif self.pick_axis == "y axis":

			self.linkPosition = [0,self.randomY/2,0]

		else:

			self.linkPosition = [0,0,self.randomZ/2]

	def Random_Joint_Axis(self):

		self.jointAxis = random.choice(["1 0 0","0 1 0","0 0 1"])










