import sud2sat as makeCNF
import sat2sud as solveSudoku
import helpers
import re
import os
import sys
import subprocess

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
                puzzle_name = match.group(1) + match.group(2)
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
        helpers.eprint("Could not get Memeory time or CPU time")
        exit(1)
    mem_used = float(mem_used_match.group(1))
    cpu_time = float(cpu_time_match.group(1))
    return dict({"memory_used": mem_used, "cpu_time": cpu_time})

def main(input_file):
    print "Starting script"
    Puzzles = open(input_file, 'r')
    if Puzzles is None:
        helpers.eprint("Could not open puzzles file.")
        exit(1)
    curr_puzzle = getNextPuzzle(Puzzles)
    data = []
    while curr_puzzle is not None:
        puzzle_data = curr_puzzle[1]
        cnf_file_name = curr_puzzle[0].strip() + "_CNF.txt"
        sat_file_name = curr_puzzle[0].strip() + "_SAT.txt"
        cnf = makeCNF.main(puzzle_data)
        cnf_file = open(cnf_file_name, "w")
        cnf_file.write(cnf)
        cnf_file.close()
        temp_file_name = "SAT_statistics.txt"
        command = "minisat "+ cnf_file_name + " " + sat_file_name + " > " + temp_file_name
        os.system(command)
        with open(temp_file_name, "r") as f:
            minisat_output = f.read()
        data_entry = parseMiniSatOutput(minisat_output)
        data_entry["Name"] = curr_puzzle[0].strip()
        data.append(data_entry)
        curr_puzzle = getNextPuzzle(Puzzles)
        if curr_puzzle is None:
            print "Puzzles processed:"
            print len(data)


        # os.system("minisat "+ cnf_file_name + " " + sat_file_name)


        

if __name__ == "__main__":
    input_file = sys.argv[1]
    main(input_file)