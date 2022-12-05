from utils import *
import re


actual_input = read_input()

def parse_input(ipt):
    crates_string, instructions_string = ipt.split("\n\n")
    crates_rows = crates_string.split("\n")
    crates_rows = crates_rows[:-1]
    n_stacks = 9
    stacks = [[] for i in range(n_stacks)]
    for row in crates_rows:
        row = [it for idx, it in enumerate(row) if (idx + 1) % (4) != 0]
        row = ["".join(row[i:i+3]) for i in range(0, len(row), 3)]
        for idx, column in enumerate(row):
            column = column.strip()
            if column:
                stacks[idx].append(column[1])
    
    instructions = [re.findall(r'\d+', s) for s in instructions_string.split("\n")]

    return stacks, instructions

def run_on_input(ipt):
    stacks, instructions = parse_input(ipt)

    for n_to_move, move_from, move_to in instructions:
        n_to_move = int(n_to_move)
        move_from = int(move_from)
        move_to = int(move_to)

        stacks[move_to - 1] = stacks[move_from - 1][:n_to_move] + stacks[move_to - 1] 
        stacks[move_from - 1] = stacks[move_from - 1][n_to_move:]  
        
    msg = "".join([stack[0] for stack in stacks])
    print(msg)
    

for ipt in [actual_input]:
    if ipt:
        run_on_input(ipt)