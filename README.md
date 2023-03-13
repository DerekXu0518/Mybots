Final project: an experiment of 3-D generated and evolved creatures 
======
This is a project based on r/ludobots MOOC.

Website: https://www.reddit.com/r/ludobots/

Used in CHEM_ENG 395 by prof. Sam Kreigman at Northwestern University in winter 2023.

A 10s gif demonstrating evolved and unevolved robots:

![alt text](https://github.com/DerekXu0518/Mybots/blob/Final_Project/Images/final%20project%20gif.gif)

A 2-min video for summary: https://youtu.be/xc9kiAossxw

## Goal

The goal of this final project is to investigate the influence of a single hidden layer on the overall locomotion of
randomly generated robots. Often time hidden layer will create a more sophisticated neuron networks and become better
handling challenging tasks. In this controlled experiment I am planning to investigate it.

Start the simulation
---
- To run the simulation, click and run `search.py`
- To test different seeds, change `seed`variable value in`constants.py`

- To obtain the fitness curve, run `analyze fitness.py`

## How to access two groups

- To access experimental group simulation, stay in `Final_Project` branch

- To access control group simulation, switch to `Final_Project_EucDistance` branch (sorry for the confusing name of the branch, I tried but failed to fina a way to rename the branch)


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
Now neuron networks will be generated in two ways:

### Control group

- All sensors are randomly generated as 50% probability on each link.

- Motors are generated on every joint.

- All sensors and motors are fully connected.

### Experimental group

- All sensors are randomly generated as 50% probability on each link.

- Motors are generated on every joint.

- A hidden layer will have 1 to 5 neurons

- All sensors are fully connected to hidden neurons and then fully connected to all motors.

![alt text](https://github.com/DerekXu0518/Mybots/blob/Final_Project/Images/Slide3.png)

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

3. Synapse weights will also change for each evolution. For experimental group, hidden neuron numbers will be randomly determined again ranging from 1 to 5.

A visual representation is shown below:

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/872209AF-8310-4622-B5ED-20D558B4F2D5_1_201_a.jpeg)

Selection
---
Selection of the parallel hill climber works as follows:

A parent and child are compared for their fitness value. If child's fitness is better than parent, replace the parent with child.
Otherwise, keep the parent. This comparison will continue for many times equal to number of generations.

For parallel hill climber, these comparison will be performed in parallel. The number of comparison happened at once equal to population size.

When all populations have selected their best parent after certain generations, these parent will be compared one by one to find the best result of the whole PHC.

A visual demonstration is shown below:

![alt text](https://github.com/DerekXu0518/Mybots/blob/Final_Project/Images/3B8FC9A5-621E-4A2F-80C0-7E04515CAF82_1_201_a.jpeg)

Parameters of simulation
---
- Population size = 10
- Number of generations = 500
- Number of robots per generation = 5000
- Number of timesteps = 1000
- Number of seeds per group = 5
- Total Simulations = 50,000

Fitness 
---
Current fitness is based on how far the robot can move in postive y-axis(y-axis value of the root link)

Two plots of fitness curves from control and experimental group are shown here.

Each point of the curve corresponds to the best parent in that generation.

![alt text](https://github.com/DerekXu0518/Mybots/blob/Final_Project/Images/Slide1.png)

## Discussion
Based on results from both control and experimental group, control group generally performs better than experimental group.
Two seeds achieve fitness around 6 and the rest are around 4. It is a little surprising to find that hidden layer does not help
the performance of experimental group but hinder it.

A possible explanation is that with current simple evolving strategy (parallel hill climber) and simple mutation methods,
an extra layer of hidden layer does not provide enough support to overall behavior but constrain the movement of the robots.
I can observe that the best one in experimental group (seed 1) has a very steady pace of movement but just slightly slower than 
control group. Control group tends to have better performance but their movements are not stable and tends to fall over. If the simulation
time step increases, the benefit of steady movements from hidden layer may be more obvious. 
Meanwhile, the current task is simple. If a more complicated task is given to the robots, experimental group may have better
performance becasue of the learning ability of hidden layer.

## Future plans
I purpose the following plans for the future:
- Increase time step to allow more behavior of robots
- Switch PHC with more efficient evolving strategy
- Give more challenging task to robots such as avoiding barriers while moving
- Increase number of seeds tested to confirm the result in a wider range.


## Acknowledgement

I want to give special thanks to our TA Donna Hooshmand and all students (especially Nic :) ) both online and offline. 
Without them, I cannot make such a big progress considering I almost had no coding experience before this class.

## In the end

Although I personally think this class is still quite immature and needs a lot of improvements, I still wish this class can continue
to give students from different background (not only CS) a chance to look at this brand-new field of study that I believe 
worth knowing for all kinds of insiprations.





