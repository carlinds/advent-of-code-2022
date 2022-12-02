from utils import *

sample1 = r"""A Y
B X
C Z"""

sample2 = r""""""

actual_input = read_input()

score_map_1 = {
    'A': 1,
    'B': 2,
    'C': 3
}

score_map_2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}
win_map = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

draw_map = {
    'A': 'A',
    'B': 'B',
    'C': 'C',
}

lose_map = {
    'A': 'C',
    'B': 'A',
    'C': 'B',
}

def run_on_input(ipt):
    rounds = [r.split() for r in ipt.split("\n")]

    tot_score = 0
    for r in rounds:
        tot_score += score_map_2[r[1]]

        if r[1] == 'X':
            choice = lose_map[r[0]]

        if r[1] == 'Y':
            choice = draw_map[r[0]]

        if r[1] == 'Z':
            choice = win_map[r[0]]
        
        tot_score += score_map_1[choice]

    print(tot_score)

for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)