import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
<<<<<<< Updated upstream
pyrosim.Send_Cube(name="Box", pos=[0,0,0.5] , size=[1,1,1])
=======
for x in range(0, 10):
    for y in range (0, 3):
        for z in range (0, 3):
            pyrosim.Send_Cube(name="Box", pos=[y, z, 0.5+x], size=[1*0.9**x, 1*0.9**x, 1*0.9**x])

>>>>>>> Stashed changes
pyrosim.End()
