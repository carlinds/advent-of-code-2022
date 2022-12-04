from utils import *

sample1 = r"""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

sample2 = r""""""

actual_input = read_input()


def run_on_input(ipt):
    rucksacks = ipt.split("\n")
    n = 3
    grps = [rucksacks[i:i+n] for i in range(0, len(rucksacks), n)]

    tot = 0
    for g in grps:
        common_char = list(set(g[0]).intersection(g[1]).intersection(g[2]))[0]

        if common_char.islower():
            tot += ord(common_char) - 96
        
        else:
            tot += ord(common_char) - 38

    print(tot)

for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)