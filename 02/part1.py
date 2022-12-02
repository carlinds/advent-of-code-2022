from utils import *

sample1 = r"""A Y
B X
C Z"""

sample2 = r""""""

actual_input = read_input()

score_map = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

wins = [
    ['A', 'Y'],
    ['B', 'Z'],
    ['C', 'X'],
]

draws = [
    ['A', 'X'],
    ['B', 'Y'],
    ['C', 'Z'],
]

def run_on_input(ipt):
    rounds = [r.split() for r in ipt.split("\n")]

    tot_score = 0
    for r in rounds:
        tot_score += score_map[r[1]]
        if r in wins:
            tot_score += 6
        elif r in draws:
            tot_score += 3

    print(tot_score)

for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)