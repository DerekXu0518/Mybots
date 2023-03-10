from parallelHillClimber import PARALLEL_HILL_CLIMBER
import random
import numpy
import constants as c
import pickle

random.seed(c.seed)

numpy.random.seed(c.seed)

phc = PARALLEL_HILL_CLIMBER()

phc.Evolve()

input("Press enter to continue...")

phc.Show_Best()

with open('bestResult.pickle', 'wb') as f:

    pickle.dump(phc, f)

    f.close()




