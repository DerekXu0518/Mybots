from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		self.parent ={}

		self.nextAvailableID = 0.0

		for i in range(0, c.populationSize):

			self.parent[i] = SOLUTION(self.nextAvailableID+1)


	def Evolve(self):

		for i in range(0, c.populationSize):

			self.parent[i].Evaluate("GUI")

#		for currentGeneration in range(1, c.numberOfGenerations):

#			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):

		self.Spawn()

		self.Mutate()

		self.child.Evaluate("DIRECT")

		self.Select()

		self.Print()


	def Spawn(self):

		self.child = copy.deepcopy(self.parent)

	def Mutate(self):

		self.child.Mutate()

	def Select(self):

		if self.parent.fitness > self.child.fitness:

			self.parent = self.child

	def Print(self):

		print(self.parent.fitness, self.child.fitness)

	def Show_Best(self):
		pass
#		os.system("python3 simulate.py GUI")