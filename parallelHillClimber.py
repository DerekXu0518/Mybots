from solution import SOLUTION
import constants as c
import copy
import os
import numpy


class PARALLEL_HILL_CLIMBER:

	def __init__(self):

		os.system("rm brain*.nndf")
		os.system("rm Fitness*.txt")
		os.system("rm body*.urdf")
		os.system("rm OverallFitness*.txt")

		self.parents ={}

		self.nextAvailableID = 0

		for i in range(c.populationSize):

			self.parents[i] = SOLUTION(self.nextAvailableID)

			self.nextAvailableID += 1

	def Evolve(self):

		self.parents[0].Start_Simulation("GUI")

		self.parents[0].Wait_For_Simulation_To_End()

		self.Evaluate(self.parents)

		for currentGeneration in range(c.numberOfGenerations):

			self.Evolve_For_One_Generation()

	def Evolve_For_One_Generation(self):

		self.Spawn()

		self.Mutate()

		self.Evaluate(self.children)

		self.Print()

		self.Write_Overall_Fitness()

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

			if self.parents[parent_key].distance < self.children[parent_key].distance:
				self.parents[parent_key] = self.children[parent_key]

	def Print(self):

		for parent_key in self.parents.keys():

			print("")

			#print("parent x: ", self.parents[parent_key].xfitness, "child x: ", self.children[parent_key].xfitness)

			#print("parent y: ", self.parents[parent_key].yfitness, "child y: ", self.children[parent_key].yfitness)

			print("parent dist: ", self.parents[parent_key].distance, "child dist: ", self.children[parent_key].distance)

			print("")

	def Show_Best(self):

		self.Best_Parent = None

		Best_Parent_xFitness = 99999

		Best_Parent_yFitness = 99999

		Best_Parent_distance = 0

		for parent_key in self.parents.keys():
			if self.parents[parent_key].distance > Best_Parent_distance:
				# Best_Parent_xFitness = self.parents[parent_key].xfitness

				# Best_Parent_yFitness = self.parents[parent_key].yfitness

				Best_Parent_distance = self.parents[parent_key].distance

				self.Best_Parent = self.parents[parent_key]

		# print("This is best xFitness and yFitness: "+str(Best_Parent_xFitness)+" and "+str(Best_Parent_yFitness))

		# print("This is the best weights:"+str(self.Best_Parent.weights))

		print("This is best distance:" + str(Best_Parent_distance))

		self.Best_Parent.Start_Simulation("GUI")


	def Evaluate(self, solutions):

		for i in range(c.populationSize):

			solutions[i].Start_Simulation("DIRECT")

		for i in range(c.populationSize):

			solutions[i].Wait_For_Simulation_To_End()

	def Write_Overall_Fitness(self):

		f = open("OverallFitness.txt", 'a')

		for parent_key in self.parents.keys():

			f.write(str(self.parents[parent_key].distance)+" ")

		f.write("\n")

		f.close()

		numpy.save("data/OveralFitness",self.parents[parent_key].distance)


