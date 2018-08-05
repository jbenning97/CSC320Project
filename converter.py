import os
import sys
import helpers

def convert_puzzle(puzzle):
    puzzle = puzzle.strip()
    if len(puzzle) != 81:
        helpers.eprint("Improper puzzle length: " + str(len(puzzle)))
        print(puzzle[len(puzzle)-1])
        exit(1)
    
    return_val = puzzle[:9] + "\n"
    return_val += puzzle[9:18] + "\n"
    return_val += puzzle[18:27] + "\n"
    return_val += puzzle[27:36] + "\n"
    return_val += puzzle[36:45] + "\n"
    return_val += puzzle[45:54] + "\n"
    return_val += puzzle[54:63] + "\n"
    return_val += puzzle[63:72] + "\n"
    return_val += puzzle[72:81] + "\n"
    return return_val

def main(input_file, output_file):
    in_file = open(input_file, "r")
    out_file = open(output_file, "w")
    grid_num = 1
    for line in in_file:
        puzzle = convert_puzzle(line)
        out_file.write("Grid " + str(grid_num) + "\n")
        out_file.write(puzzle +"\n")
        grid_num += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        helpers.eprint("Command format: python master.py <input_file_name> <output_file_name>")
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)