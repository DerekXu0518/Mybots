from solution import SOLUTION
import constants as c
import copy
import os


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		os.system("rm brain*.nndf")
		os.system("rm Fitness*.txt")

		self.parents ={}

		self.nextAvailableID = 0

		for i in range(c.populationSize):

			self.parents[i] = SOLUTION(self.nextAvailableID)

			self.nextAvailableID += 1

	def Evolve(self):

		self.parents[0].Start_Simulation("GUI")

		self.parents[0].Wait_For_Simulation_To_End()

		exit()

		self.Evaluate(self.parents)

		for currentGeneration in range(c.numberOfGenerations):

			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):

		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		self.Print()

		self.Select()

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

		for parent_key in self.parents.keys():

			if self.parents[parent_key].xfitness > self.children[parent_key].xfitness and abs(self.parents[parent_key].yfitness) < abs(self.parents[parent_key].yfitness):

				self.parents[parent_key] = self.children[parent_key]

	def Print(self):

		for parent_key in self.parents.keys():

			print("")

			print("parent x: ", self.parents[parent_key].xfitness, "child x: ", self.children[parent_key].xfitness)

			print("parent y: ", self.parents[parent_key].yfitness, "child y: ", self.children[parent_key].yfitness)

			print("")

	def Show_Best(self):

		self.Best_Parent = None

		Best_Parent_xFitness = 99999

		Best_Parent_yFitness = 99999

		for parent_key in self.parents.keys():

			if self.parents[parent_key].xfitness < Best_Parent_xFitness:

				Best_Parent_xFitness = self.parents[parent_key].xfitness

				Best_Parent_yFitness = self.parents[parent_key].yfitness

				self.Best_Parent = self.parents[parent_key]

		print("This is best xFitness and yFitness: "+str(Best_Parent_xFitness)+" and "+str(Best_Parent_yFitness))

		#print("This is the best weights:"+str(self.Best_Parent.weights))

		self.Best_Parent.Start_Simulation("GUI")

	def Evaluate(self, solutions):

		for i in range(c.populationSize):

			solutions[i].Start_Simulation("DIRECT")

		for i in range(c.populationSize):

			solutions[i].Wait_For_Simulation_To_End()


