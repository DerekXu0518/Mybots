import pybullet as p
import time

physicsClient = p.connect(p.GUI)
for t in range(1,1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(t)
p.disconnect()

