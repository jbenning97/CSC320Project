# CSC320 Project
Summer 2018 - Bruce Kapron

An exercise in SAT solvers.

### Group Members
* Jordan Benning
* Jerusha Chua
* Braiden Cutforth
* Purvika Dutt

## Basic Task

### master
Reads a sudoku puzzle file with many sudoku puzzles in the format:
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
```
and outputs a file with the solved sudoku puzzles in the format:
```
Grid 01
483921657
967345821
251876493
548132976
729564138
136798245
372689514
814253769
695417382
Time to solve: 0.005067 s
Memory used to solve: 0.63 MB
```

Additionally it will output the number of puzzles processed, average CPU used and average memory used.

#### How it works
master.py starts by reading in puzzles from a specified input file. For each puzzle it invokes sud2sat, then passes the CNF to the minisat. Once minisat is done, the stdout output is parsed and the execution time and memory used are read. The file that was output by minisat is then read by sat2sud which creates the solved sudoku. Once we have the solved sudoku we append it to the output file and add the time it took and the memeory that was used to solve that puzzle. Once every puzzle is solved we output the number of puzzles we solved, the average time to solve them and the average amount of memory used.

### sud2sat
Reads a Sudoku puzzle and converts it to CNF formula suitable for input to the miniSAT solver.

### sat2sud
Reads the output produced by miniSAT for the given puzzle instance and converts it back into a solved Sudoku puzzle.
