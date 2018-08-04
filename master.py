import sud2sat as makeCNF
import sat2sud as solveSudoku
import helpers
import os

def main():
    print "Starting script"
    Puzzles = open('samplesudoku.txt', 'r')
    if Puzzles is None:
        helpers.eprint("Could not open puzzles file.")
    
    
        

if __name__ == "__main__":
    
    main()