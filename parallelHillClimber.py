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

		self.parents ={}

		self.nextAvailableID = 0

		for i in range(c.populationSize):

			self.parents[i] = SOLUTION(self.nextAvailableID)

			self.nextAvailableID += 1

	def Evolve(self):

		self.Evaluate(self.parents)

		for currentGeneration in range(c.numberOfGenerations):

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

		for parent in self.parents.keys():

			self.children[parent] = copy.deepcopy(self.parents[parent])

			self.children[parent].Set_ID(self.nextAvailableID)

			self.nextAvailableID += 1

	def Mutate(self):

		for child in self.children.keys():

			self.children[child].Mutate()

	def Select(self):

		if self.parents.fitness > self.children.fitness:

			self.parents = self.child

	def Print(self):

		print(self.parents.fitness, self.children.fitness)

	def Show_Best(self):

		pass
		os.system("python3 simulate.py GUI")

	def Evaluate(self, solutions):

		for i in range(c.populationSize):

			solutions[i].Start_Simulation("DIRECT")

		for i in range(c.populationSize):

			solutions[i].Wait_For_Simulation_To_End()


