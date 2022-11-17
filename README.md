# Google_foobar_challenge
This repository contains my solutions to Google Foobar challenge.
**I'll be uploading solutions over few days in quite random order...**

## Challenges

**1-1 Skipping Work**
  
Given two almost identical lists of worker IDs x and y where one of the lists contains an additional ID, 
write a function solution(x, y) that compares the lists and returns the additional ID.

For example, given the lists x = [13, 5, 6, 2, 5] and y = [5, 2, 5, 13], 
the function solution(x, y) would return 6 because the list x contains the integer 6 and the list y doesn't. 
Given the lists x = [14, 27, 1, 4, 2, 50, 3, 1] and y = [2, 4, -4, 3, 1, 1, 14, 27, 50], 
the function solution(x, y) would return -4 because the list y contains the integer -4 and the list x doesn't.

In each test case, the lists x and y will always contain n non-unique integers where n is at least 1 but never more than 99,
and one of the lists will contain an additional unique integer which should be returned by the function. 
The same n non-unique integers will be present on both lists, 
but they might appear in a different order like in the examples above. 
Commander Lambda likes to keep the numbers short, so every worker ID will be between -1000 and 1000.  

_________________________________
**2-1 Power hungry**

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power.
Huge space stations with doomsday devices take even more power. 
To help meet the station's power needs, Commander Lambda has installed solar panels on the station's outer surface. 
But the station sits in the middle of a quasar quantum flux field, which wreaks havoc on the solar panels. 
You and your team of henchmen has been assigned to repair the solar panels, 
but you can't take them all down at once without shutting down the space station (and all those pesky life support systems!).

You need to figure out which sets of panels in any given array you can take offline 
to repair while still maintaining the maximum amount of power output per array, 
and to do THAT, you'll first need to figure out what the maximum output of each array actually is. 
Write a function answer(xs) that takes a list of integers representing the power output levels of each panel in an array, 
and returns the maximum product of some non-empty subset of those numbers. 
So for example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], 
then the maximum product would be found by taking the subset: 
    xs[0] = 2, xs[1] = -3, xs[4] = -5,   
    giving the product 2*(-3)*(-5) = 30.   
    So answer([2,-3,1,0,-5]) will be "30".  

Each array of solar panels contains at least 1 and no more than 50 panels, 
and each panel will have a power output level whose absolute value is no greater than 1000 
(some panels are malfunctioning so badly that they're draining energy, 
 but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to produce 
 the positive output of the multiple of their power values). 
The final products may be very large, so give the answer as a string representation of the number.

Test cases:  
Inputs:  
x = [2, 0, 2, 2, 0]  
Output:  
"8"  
  
Inputs:  
x = [-2, -3, 4, -5]  
Output:  
"60"  
  
_________________________________  
**2-2 Bunny Prisoner Locating**

Keeping track of Commander Lambda's many bunny prisoners is starting to get tricky. You've been tasked with writing a program to match bunny prisoner IDs to cell locations.  

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:  
  
| 7  
| 4 8  
| 2 5 9  
| 1 3 6 10  
  
Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground. 
  
For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely (Commander Lambda has been taking a LOT of prisoners). 
  
Write a function answer(x, y) which returns the prisoner ID of the bunny at location (x, y). Each value of x and y will be at least 1 and no greater than 100,000. Since the prisoner ID can be very large, return your answer as a string representation of the number.
  
Test cases:
  
Inputs:  
x = 3  
y = 2  
Output:  
"9"  
  
Inputs:  
x = 5  
y = 10  
Output:  
"96"  
_________________________________
**3-2 Bomb, Baby!**  
  
You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two distinct processes: Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created; Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!)

You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.

Test cases:  
Input:  
solution.solution('4', '7')  
Output:  
    4  

Input:  
solution.solution('2', '1')  
Output:  
    1  
_________________________________
**4-1 Bringing a Gun to a Trainer Fight**
  
Write a function solution(dimensions, your_position, trainer_position, distance) 
that gives an array of 2 integers of the width and height of the room, 
an array of 2 integers of your x and y coordinates in the room, 
an array of 2 integers of the trainer's x and y coordinates in the room, 
and returns an integer of the number of distinct directions that you can fire to hit the elite trainer, 
given the maximum distance that the beam can travel.
  
The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. 
You and the elite trainer are both positioned on the integer lattice at different distinct positions (x, y) 
inside the room such that [0 < x < x_dim, 0 < y < y_dim]. 
Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 
1 < distance <= 10000.
  
For example, if you and the elite trainer were positioned in a room with dimensions [3, 2],
your_position [1, 1], trainer_position [2, 1], and a maximum shot distance of 4, 
you could shoot in seven different directions to hit the elite trainer 
(given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. 
As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1,
the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite trainer
with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting 
the elite trainer with a total shot distance of sqrt(5).

Test cases:  
Input:  
solution.solution([3,2], [1,1], [2,1], 4)  
Output:  
    7  

Input:  
solution.solution([300,275], [150,150], [185,100], 500)  
Output:  
    9  
    
_________________________________

**5-1 Expanding Nebula**  

You've escaped Commander Lambda's exploding space station along with numerous escape pods full of bunnies. 
But -- oh no! -- one of the escape pods has flown into a nearby nebula, causing you to lose track of it. 
You start monitoring the nebula, but unfortunately, just a moment too late to find where the pod went. 
However, you do find that the gas of the steadily expanding nebula follows a simple pattern, 
meaning that you should be able to determine the previous state of the gas and narrow down where you might find the pod.

From the scans of the nebula, you have found that it is very flat and distributed in distinct patches, 
so you can model it as a 2D grid. 
You find that the current existence of gas in a cell of the grid is determined exactly by its 4 nearby cells, 
specifically, (1) that cell, (2) the cell below it, (3) the cell to the right of it, 
and (4) the cell below and to the right of it. 
If, in the current state, exactly 1 of those 4 cells in the 2x2 block has gas, 
then it will also have gas in the next state. Otherwise, the cell will be empty in the next state.

For example, let's say the previous state of the grid (p) was:
.O..  
..O.  
...O  
O...  
  
To see how this grid will change to become the current grid (c) over the next time step, 
consider the 2x2 blocks of cells around each cell.  
Of the 2x2 block of [p[0][0], p[0][1], p[1][0], p[1][1]], only p[0][1] has gas in it, 
which means this 2x2 block would become cell c[0][0] with gas in the next time step:
.O -> O  
..  
  
Likewise, in the next 2x2 block to the right consisting of [p[0][1], p[0][2], p[1][1], p[1][2]], 
two of the containing cells have gas, so in the next state of the grid, c[0][1] will NOT have gas:
O. -> .  
.O  
  
Following this pattern to its conclusion, from the previous state p, the current state of the grid c will be:
O.O  
.O.  
O.O  
  
Note that the resulting output will have 1 fewer row and column, 
since the bottom and rightmost cells do not have a cell below and to the right of them, respectively.

Write a function solution(g) where g is an array of array of bools saying whether there is gas in each cell 
(the current scan of the nebula), and return an int with the number of possible previous states that 
could have resulted in that grid after 1 time step.  
For instance, if the function were given the current state c above, 
it would deduce that the possible previous states were p (given above) as well as its horizontal and vertical reflections, 
and would return 4. The width of the grid will be between 3 and 50 inclusive, 
and the height of the grid will be between 3 and 9 inclusive.  
The solution will always be less than one billion (10^9).

Test cases:  
Input:  
solution.solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]])  
Output:  
11567  
  
Input:  
solution.solution([[True, False, True], [False, True, False], [True, False, True]])  
Output:  
4

Input:
solution.solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]])
Output:
    254
"""
