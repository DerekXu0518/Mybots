from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import numpy
import constants as c


random.seed(c.seed)

numpy.random.seed(c.seed)

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

input("Press enter to continue...")

phc.Show_Best()


