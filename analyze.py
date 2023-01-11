import numpy
import matplotlib.pyplot

# retrieve sensor value
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# plot data
line1 = matplotlib.pyplot.plot(backLegSensorValues, linewidth=4, label="backLegSensorValues")
line2 = matplotlib.pyplot.plot(frontLegSensorValues, label="frontLegSensorValues")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
