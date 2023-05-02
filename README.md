# Pi-in-the-Sky
The "Flying Fish"

## Assignment Description

We want to fire a projectile out of Mr. Miller's air cannon that can withold up to 100 psi of pressure. We want our payload to achieve the greatest possible velocity upon launch.

# Planning

## Initial Research
While researching we've learned to make sure that the center of pressure of our "mortar" needs to be behind the center of mass.
![69-Figure5 1-1](https://user-images.githubusercontent.com/71406930/206541266-537109b3-7495-439d-a1c5-15fe138c060b.png)

We will find the equation for velocity over time V(T) and plot it on a Velocity/Time graph. Then we will use both derivative tests to find the maximum/minimum points as well as points of concavity. 


## Initial Brainstorming
We've decided to use the teardrop shape for the main body as it is the most aerodynamic. Also, we are going to add fins to stabilize so it doesnt flip and tumble in the air.



## Initial Designing
![notamortar diagram](https://user-images.githubusercontent.com/71406930/206541329-ee17906f-74d8-41f4-a5e7-0f06507d06c8.PNG)


-inside diameter of largest part of the rocket is 65.43mm 

## Code
![block](https://user-images.githubusercontent.com/71406930/206541149-1e0acf0c-7bb9-4517-93df-484c7a67a0a0.PNG)

## Air cannon

Middle opening in the larger pvc pipe is 3.042 inches, smaller pvc pipe is 2.047 inches. 

## Risk Mitigation

We will wear proper PPE during all test and final launches as well as keep the projectile safe betweeen launches. Before firing at 100 psi we will do test launches starting from as low as 20 psi. We will also do our best to not fire at homes.

## Data

Spring is 87.5mm by 21.5mm. Inside of spring's diameter is 17mm.
Inside holes for where circuit board screws go are 2.8mm

Diameter for inside of screw holes for circuit board are 2.8mm
# Timeline (10 weeks)

## First 2 weeks

Onshape design + CFD 

<img src="Images/dsihgkifdjxhjdo.PNG" width="300">

## Next 3 weeks

Learning + Creating ciruit board

Circuit board itself is 109.3mm by 54mm without modules
Circuit board with modules is 120.5mm by 54.1mm

<img src="Images/fsef3w6sgd(final).jpg" width="1">

<img src="Images/TopOfBoard.jpeg" width="400">

<img src="Images/BottomOfBoard.jpeg" width="400">

## Next 2 weeks 

Coding/Testing

[GPS Module](rapsberry/gpsmodule.py)

[Accelerometer](rapsberry/accelerometer.py)

## Last 3 weeks 

Trials/Tribulations

Now found out we need a button or switch to change the pico from a Data collecting mode to a Data saving mode

always have forceps or needle nose pliers on hand if you are changing something to the circuit board while its in the payload bay because your fat fingers are not fitting that far into the bay.

# Launch day 4/17

Immediately tumbled, landed on its side but did not shatter on outside. Inside however had multiple broken parts. Need to add more weight in tip compartment to prevent further tumble.

Filled tip and head of the rocket with copper bbs for more weight support.

## Post launch days

Printed new mid section for rocket with more supports. Also changed the wire inside to a switch so we could easily change between data or code mode. 

## Rest of time

Collect data, rework designs with onshape and physical creations, launch again
