3-D generated creatures
======
This is a project based on r/ludobots MOOC.

Website: https://www.reddit.com/r/ludobots/

Used in CHEM_ENG 395 by prof. Sam Kreigman at Northwestern University in winter 2023.

10s video for randomly generated creatures: https://youtu.be/aL19Hq6LgS4

Start the simulation
---
To run the simulation, click and run search.py


## Body

### Genotype

Each creature has one root link and a leg that will be randomly generated into free space.

Here is the visual demonstration:

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/IMG_0051.jpeg)

### Ontology

The body of the creatures ranges from 4 to 10 links. Each non-root link can expand in +x, +y and +z direction.

The visual ontology will be the picture below:

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/IMG_0052.jpeg)

Neuron Networks
---
All sensors are randomly generated as 50% probability on each link.

Motors are generated on every joint.

All sensors and motors are currently fully connected.

![alt text](https://github.com/DerekXu0518/Mybots/blob/3D_snake/Images/IMG_0053.jpeg)

Fitness 
---
There is no fitness function used currently.

## Acknowledgement

I want to give special thanks to our TA Donna Hooshmand and all students (especially Nic :) ) both online and offline. 
Without them, I cannot make such a big progress considering I almost had no coding experience before this class.




