from solution import SOLUTION
import constants as c
import copy
import os
import glob


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		#for b in glob.glob("brain*.nndf"):

		#	os.remove(b)

		#for f in glob.glob("Fitness*.txt"):

		#	os.remove(f)

		self.parent ={}

		self.nextAvailableID = 0

		for i in range(0, c.populationSize):

			self.parent[i] = SOLUTION(self.nextAvailableID)

			self.nextAvailableID += 1

	def Evolve(self):

		self.Evaluate(self.parent)

		for currentGeneration in range(1, c.numberOfGenerations):

			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):

		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		exit()

		#self.Select()

		#self.Print()

	def Spawn(self):

		self.children = {}

		for i in range(0, c.populationSize):

			self.children[i] = copy.deepcopy(self.parent[i])

			self.children[i].Set_ID(self.nextAvailableID)

			self.nextAvailableID += 1.0

	def Mutate(self):

		for i in range(0, c.populationSize):

			self.children[i].Mutate()

	def Select(self):

		if self.parent.fitness > self.child.fitness:

			self.parent = self.child

	def Print(self):

		print(self.parent.fitness, self.child.fitness)

	def Show_Best(self):

		pass
		os.system("python3 simulate.py GUI")

	def Evaluate(self, solutions):

		for i in range(0, c.populationSize):

			solutions[i].Start_Simulation("GUI")

		for i in range(0, c.populationSize):

			solutions[i].Wait_For_Simulation_To_End()


