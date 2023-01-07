import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[3, 3, 0.5], size=[1, 1, 1])
    pyrosim.End()

def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="torso", pos=[1.5, 0, 1.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_backleg", parent="torso", child="backleg", type="revolute", position=[1, 0, 1])
    pyrosim.Send_Cube(name="backleg", pos=[-0.5, 0, -0.5], size=[1, 1, 1])
    pyrosim.Send_Joint(name="torso_frontleg", parent="torso", child="frontleg", type="revolute", position=[2, 0, 1])
    pyrosim.Send_Cube(name="frontleg", pos=[0.5, 0, -0.5], size=[1, 1, 1])

    pyrosim.End()

#Call both functions
Create_World()
Create_Robot()
