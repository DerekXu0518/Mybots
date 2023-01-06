import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
for x in range(0, 10):
    for y in range (0, 3):
        for z in range (0, 3):
            pyrosim.Send_Cube(name="Box", pos=[y, z, 0.5+x], size=[1*0.9**x, 1*0.9**x, 1*0.9**x])

pyrosim.End()
