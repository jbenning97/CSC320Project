import sys

def main(in_string):
    lines = in_string.splitlines()
    is_solved = lines[0].strip()
    solved_puzzle = ""
    if is_solved == 'SAT':
        vars = lines[1]
        list_vars = vars.split(" ")
        for x in range(len(list_vars)):
            list_vars[x] = int(list_vars[x])
        for y in range(9):
            row = ''
            for x in range(9):
                for z in range(9):
                    if list_vars[y*81 + 9*x + z] >= 0:
                        row += str(z + 1)
                        break
            solved_puzzle += row + "\n"
    else:
        solved_puzzle += "The sudoku puzzle in the represented CNF is unsatisfiable\n"

    return solved_puzzle


if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, "r") as in_f:
        input_data = in_f.read()
    if len(sys.argv) != 3:
        helpers.eprint("Invalid format. Please use format: \"python sud2sat.py input.txt output.txt\"")
        sys.exit()
    with open(output_file, "w") as out_f:
        out_f.write(main(input_data))
        out_f.close()