import numpy
import matplotlib.pyplot as plt

# retrieve .npy files
#backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
#backLegTargetAngles = numpy.load("data/backLegTargetAngles.npy")
#frontLegTargetAngles = numpy.load("data/frontLegTargetAngles.npy")
with open('OverallFitness.txt', 'r') as file:
    data = []
    for line in file:
        row = [float(x) for x in line.split()]
        data.append(row)

max_values = []
for sublist in data:
    max_value = max(sublist)
    max_values.append(max_value)


# plot data
#matplotlib.pyplot.plot(backLegTargetAngles, label="backLeg")
#matplotlib.pyplot.plot(frontLegTargetAngles, label="frontLeg")
#line1 = matplotlib.pyplot.plot(backLegSensorValues, linewidth=4, label="backLegSensorValues")
#line2 = matplotlib.pyplot.plot(frontLegSensorValues, label="frontLegSensorValues")
plt.plot(range(1, len(max_values) + 1), max_values)
plt.xlabel('Generations')
plt.ylabel('Best Fitness')
plt.title('Fitness curve over generations')
plt.xticks(range(1, len(max_values) + 1))
plt.show()



