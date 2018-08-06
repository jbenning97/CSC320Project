# CSC320 Project
Summer 2018 - Bruce Kapron

An exercise in SAT solvers.

### Group Members
* Jordan Benning V00853079
* Jerusha Chua V00840826
* Braiden Cutforth V00853754
* Purvika Dutt V00849852

## Basic Task

### sud2sat
Reads a Sudoku puzzle and converts it to CNF formula suitable for input to the miniSAT solver. Can be run via command line in the following format:
```
python sud2sat.py input.txt output.txt
```
where input.txt is a file that contains a single Sudoku puzzle having the following format:
```
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
```
and output.txt is the file to which the program will write the corresponding CNF in the DIMACS format for the SAT solver.

### sat2sud
Reads the output produced by miniSAT for the given puzzle instance and converts it back into a solved Sudoku puzzle. Can be run via command line in the following format:
```
python sat2sud.py input.txt output.txt
```
where input.txt is a the SAT solution produced by miniSAT, and output.txt is the file to which the program will write the solved Sudoku (if miniSAT concluded that the provided CNF is satisfiable).

### master
To make it easier to test the 50 puzzles in the basic task, master.py is a script that can be run via command line in the following format:
```
python master.py input.txt output.txt
```
Where input.txt is the list of the puzzles used for the basic task encoded as:
```
Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300

Grid 02
...
```
and output.txt is a file the user can designate for the solved puzzles to be written to, along with number of puzzles processed, average CPU used and average memory used for each puzzle.

### Converter
Use like:
`python converter.py input.txt output.txt`

Takes an input file of puzzles encoded as:
```
4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......
```
Outputs a file in the format:
```
Grid 1
4.....8.5
.3.......
...7.....
.2.....6.
....8.4..
....1....
...6.3.7.
5..2.....
1.4......
```

### Helpers
This file is purely used to make functions available to all other python files. Specifically it contains an eprint function which prints out to stderr

### __init__
This file is empty but required by python so the python compiler looks for imports in the current directory.
See the documentation [here](https://docs.python.org/3/tutorial/modules.html#packages) for more details.

#### How it works
master.py starts by reading in puzzles from a specified input file. For each puzzle it invokes sud2sat, then passes the CNF to the minisat. Once minisat is done, the stdout output is parsed and the execution time and memory used are read. The file that was output by minisat is then read by sat2sud which creates the solved sudoku. Once we have the solved sudoku we append it to the output file and add the time it took and the memeory that was used to solve that puzzle. Once every puzzle is solved we output the number of puzzles we solved, the average time to solve them and the average amount of memory used.

## Extended Tasks

### Extended Task 1
For this task the hard puzzles were solved. The solved puzzles appear in the report. In order to execute this task, converter.py was used to convert to the proper encoding. Then master.py was used to solve all the puzzles simultaneously and retrieve their solutions.

### Extended Task 2
For this task, an alternate encoding is used. In order to run this differently than the basic task, the program alt_sud2sat.py can be ran instead of sud2sat.py (they accept the same input format) via the command line in the following format:
```
python alt_sud2sat.py input.txt output.txt
```

### Extended Task 3
For this task an alternate SAT solver was used, cryptominisat. The source code for cryptominisat can be found [here](https://github.com/msoos/cryptominisat). For this task data was collected and is present in the report.
