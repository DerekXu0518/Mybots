import pickle

with open('bestResult.pickle', 'rb') as f:

    phc = pickle.load(f)

    f.close()

phc.Show_Best()