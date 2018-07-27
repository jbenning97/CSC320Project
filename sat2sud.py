def main():
    sat_f = open("SATsolution.txt", "r")
    is_solved = sat_f.readline().strip()
    solved_f = open("solvedSudoku.txt", "w")
    if is_solved == 'SAT':
        vars = sat_f.readline()
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
            solved_f.write(row + "\n")
    else:
        solved_f.write("The soduku puzzle in the represented CNF is unsatisfiable\n")
    sat_f.close()
    solved_f.close()


if __name__ == "__main__":
    main()