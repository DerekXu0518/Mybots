3-D generated and evolved creatures 
======
This is a project based on r/ludobots MOOC.

Website: https://www.reddit.com/r/ludobots/

Used in CHEM_ENG 395 by prof. Sam Kreigman at Northwestern University in winter 2023.

10s video for evolution of 3D creatures: https://youtu.be/I9IPIa3FQuU

Start the simulation
---
To run the simulation, click and run search.py


## Body

### Genotype

Each creature has one root link and a leg that will be randomly generated into free space.

Here is the visual demonstration:

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/IMG_0051.jpeg)

### Ontology

The body of the creatures ranges from 4 to 6 links. Each non-root link can expand in a certain pattern demonstrated in the picture below.
Specifically. If previous link is grow in +x, then the next will choose to grow in either +y or +z direction. Similar if previous link is in +y or +z direction.
In this way, no three continuous links will be in the same axis, so that the overall body can achieve relative complexity in 3D space, not forming a flat snake.

The visual ontology will be the picture below:

Note that the second leg can be created as either red or blue

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/37F32942-D5AA-434E-AD8B-A67177B96EC5_1_201_a.jpeg)

Neuron Networks
---
All sensors are randomly generated as 50% probability on each link.

Motors are generated on every joint.

All sensors and motors are currently fully connected.

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/IMG_0053.jpeg)

Mutation
---
Several mutations will perform for each evolution:

1. One random link(excluding the first and last one) will be chosen and changes as following:

If it has sensor then remove this sensor. If not, add a sensor to this link. 

Change the size of this link 

Change the joint axis before this link

2. With 50% probability, one of following actions will take place:

A link will add at the end of the chain, with similar way as the main body. It can grow in  +x, +y; +x, +z or +y, +z 
directions depending on the orientation of previous link so that no three continuous links are located in the same axis.

or

A link at the end of chain will be removed with the corresponding joint.

3. Synapse weights will also change for each evolution.

A visual representation is shown below:

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/872209AF-8310-4622-B5ED-20D558B4F2D5_1_201_a.jpeg)


Fitness 
---
Current fitness is based on how far the robot can move in postive y-axis(y-axis value of the root link)

A plot of five fitness curves  using 1-5 seeds is shown below. Due to time constraint and computer limitation, current population are 10 and generations are 50.
This will increase for future final project to demonstrate more apparent evolution.

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/Figure_1.png)

## Acknowledgement

I want to give special thanks to our TA Donna Hooshmand and all students (especially Nic :) ) both online and offline. 
Without them, I cannot make such a big progress considering I almost had no coding experience before this class.




