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
