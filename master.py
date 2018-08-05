import sud2sat as makeCNF
import sat2sud as solveSudoku
import helpers
import re
import os
import sys
import subprocess
import traceback

def getNextPuzzle(myFile):
    puzzle_heading = re.compile(r"([Gg]rid) (\d*)")
    puzzle_name = ""
    puzzle = ""
    last_pos = myFile.tell()
    while True:
        line = myFile.readline()
        if line == "":
            break
        match = puzzle_heading.match(line)
        if match:
            if puzzle_name == "":
                puzzle_name = match.group(0)
            else:
                myFile.seek(last_pos)
                break
        elif line == "\n":
            continue
        else:
            puzzle += line
        last_pos = myFile.tell()
    
    if puzzle_name == "":
        return None
    else:
        return [puzzle_name, puzzle]

def parseMiniSatOutput(output):
    # print output
    mem_used_re = re.compile(r"Memory used\s*:\s*(\d*.\d*)\s*MB")
    cpu_time_re = re.compile(r"CPU time\s*:\s*(\d*.\d*)\s*s")
    mem_used_match = mem_used_re.search(output)
    cpu_time_match = cpu_time_re.search(output)
    if not mem_used_match or not cpu_time_match:
        traceback.print_stack()
        helpers.eprint("Could not get Memory time or CPU time")
        exit(1)
    mem_used = float(mem_used_match.group(1))
    cpu_time = float(cpu_time_match.group(1))
    return dict({"memory_used": mem_used, "cpu_time": cpu_time})

def main(input_file, output_file):
    print "Starting script"
    Puzzles = open(input_file, 'r')
    if Puzzles is None:
        helpers.eprint("Could not open puzzles file.")
        exit(1)
    curr_puzzle = getNextPuzzle(Puzzles)
    data = []
    Solved_Puzzles = open(output_file, 'w')
    while curr_puzzle is not None:
        puzzle_data = curr_puzzle[1]
        cnf_file_name = curr_puzzle[0].replace(" ","") + "_CNF.txt"
        sat_file_name = curr_puzzle[0].replace(" ","") + "_SAT.txt"
        cnf = makeCNF.main(puzzle_data)
        with open(cnf_file_name, "w") as f:            
            f.write(cnf)
        temp_file_name = "SAT_statistics.txt"
        command = "minisat "+ cnf_file_name + " " + sat_file_name + " > " + temp_file_name
        os.system(command)
        with open(temp_file_name, "r") as f:
            minisat_output = f.read()
        data_entry = parseMiniSatOutput(minisat_output)
        data_entry["Name"] = curr_puzzle[0].strip()
        data.append(data_entry)
        with open(sat_file_name, "r") as f:
            sat = f.read()
        solved_puzzle = solveSudoku.main(sat)
        Solved_Puzzles.write(curr_puzzle[0]+ "\n")
        Solved_Puzzles.write(solved_puzzle)
        Solved_Puzzles.write("\n")
        os.system("rm " + cnf_file_name + " " + sat_file_name + " " + temp_file_name)
        curr_puzzle = getNextPuzzle(Puzzles)
        if curr_puzzle is None:
            print "Puzzles processed:"
            print len(data)
    
    Puzzles.close()
    Solved_Puzzles.close()

    num_entries = len(data)
    MB_used = 0
    CPU_used = 0
    quickest_time = 1
    for entry in data:
        MB_used += entry["memory_used"]
        CPU_used += entry["cpu_time"]
        if entry["cpu_time"] < quickest_time:
            quickest_time = entry["cpu_time"]
    
    print quickest_time
    MB_used = MB_used/num_entries
    CPU_used = CPU_used/num_entries
    print "Average CPU usage: " + str(CPU_used) + " s"
    print "Average memory usage: " + str(MB_used) + " MB"


        # os.system("minisat "+ cnf_file_name + " " + sat_file_name)


        

if __name__ == "__main__":
    if len(sys.argv) != 3:
        helpers.eprint("Command format: python master.py <input_file_name> <output_file_name>")
        exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)