# Project for the Module BTI7541a Python <br>
### Semester Spring 2021
#### Made by Céline Hüttenmoser (HUTTC2) at the BFH.

#### Mazes
In this project, a maze can be read from a text file. 
The program will search for the path from a starting point A to an end point B.<br>
At the end, the maze will be printed showing the path with the coordinates.<br>

Furthermore, cycles can be printed and visualised in the maze. Visited points on which the algorithm had to returned can also be visible inside the maze.<br>

The encoding is as follows:<br>
```python
'*': 0,  # wall <br>
' ': 1,  # free space<br>
'A': 2,  # starting point<br>
'B': 3,  # end point<br>
'S': 4,  # south<br>
'N': 5,  # north<br>
'E': 6,  # east<br>
'W': 7,  # west<br>
'R': 9,  # returned<br>
'C': 10  # cycle <br>
```

#### Starting the program

The program can be started with the command line as follows:<br>
`>python3 maze.py <maze-file.txt>` <br>
where <maze-file.txt> is the chosen text file for the maze.

#### Environment

This program needs python 3.8 and uses the library Numpy.
