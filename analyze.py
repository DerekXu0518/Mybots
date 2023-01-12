import numpy
import matplotlib.pyplot

# retrieve .npy files
backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
backLegTargetAngles = numpy.load("data/backLegTargetAngles.npy")
frontLegTargetAngles = numpy.load("data/frontLegTargetAngles.npy")

# plot data
matplotlib.pyplot.plot(backLegTargetAngles, label="backLeg")
matplotlib.pyplot.plot(frontLegTargetAngles, label="frontLeg")
#line1 = matplotlib.pyplot.plot(backLegSensorValues, linewidth=4, label="backLegSensorValues")
#line2 = matplotlib.pyplot.plot(frontLegSensorValues, label="frontLegSensorValues")

matplotlib.pyplot.legend()
matplotlib.pyplot.show()
