import os

def to_nineary(x,y,z):
    return (x-1)*81 + (y-1)*9 + (z-1) + 1


def main():
    # Encoding sudoku puzzle into string
    with open("samplesudoku.txt") as f:
        lines = f.read().splitlines()
        encoded_puzzle = ""
        for i in range(1,10):
            encoded_puzzle += lines[i]
        f.close()

    # Creating matrix from encoded puzzle
    matrix = [[0 for x in range(9)] for y in range(9)]
    for x in range(9):
        for y in range(9):
            # This will fail if we use ? etc as wild character
            temp = encoded_puzzle[x*9+y]
            if(temp in ['.','*','?']):
                temp = 0
            matrix[x][y] = int(temp)

    print(matrix)
    # Write first line of CNF
    variables = 0
    cnf = open("sudokuCNF.txt", "w")
    for x in range(9):
        for y in range(9):
            if matrix[x][y] != 0:
                variables += 1
    cnf.write("p cnf 729 " + str(8829 + variables) + "\n")



    # Write clauses for existing sudoku values
    for x in range(9):
        for y in range(9):
            if matrix[x][y] not in [0,'.','*','?']:
                cnf.write(str(to_nineary(x+1, y+1, int(matrix[x][y]))) + " 0\n")

    # Write clauses for constraint: There is at least one number in each entry
    # ie. There is at least a number [1-9] in each cell of the sudoku
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                cnf.write(str(to_nineary(x, y, z)) + " ")
            cnf.write(" 0\n")

    # Write clauses for constraint: Each number appears at most once in each column
    for x in range(1, 10):
        for z in range(1, 10):
            for y in range(1, 9):
                for i in range(y + 1, 10):
                    cnf.write("-" + str(to_nineary(x, y, z)) + " -" + str(to_nineary(x, i, z)) + " 0\n")

    # Write clauses for constraint: Each number appears at most once in each row
    for y in range(1, 10):
        for z in range(1, 10):
            for x in range(1,9):
                for i in range(x + 1, 10):
                    cnf.write("-" + str(to_nineary(x, y ,z)) + " -" + str(to_nineary(i, y, z)) + " 0\n")

    # Write clauses for constraint: Each number appears at most once in each 3x3 sub-grid
    for z in range(1,10):
        for i in range(0,3):
            for j in range(0,3):
                for x in range(1,4):
                    for y in range(1,4):

                        for k in range(y + 1, 4):
                            cnf.write("-" + str(to_nineary((3*i) + x, (3*j) + y, z)) + " -" + str(to_nineary((3*i) + x, (3*j) + k, z)) + " 0\n")

                        for k in range(x + 1, 4):
                            for l in range(1, 4):
                                cnf.write("-" + str(to_nineary((3*i) + x, (3*j) + y, z)) + " -" + str(to_nineary((3*i) + k, (3*j) + l, z)) + " 0\n")


    # Done writing clauses. Run minisat solver on completed CNF
    cnf.close()
    os.system("minisat sudokuCNF.txt SATsolution.txt")

if __name__ == "__main__":
    main()