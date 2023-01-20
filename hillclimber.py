from solution import SOLUTION
import constants as c
import copy
import os


class HILL_CLIMBER:

	def __init__(self):

		self.parent = SOLUTION()

	def Evolve(self):

		self.parent.Evaluate("GUI")

		for currentGeneration in range(1, c.numberOfGenerations):

			self.Evolve_For_One_Generation()

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

		os.system("python3 simulate.py GUI")