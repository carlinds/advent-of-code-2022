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
    compartments = [(l[:int(len(l)/2)], l[int(len(l)/2):]) for l in rucksacks]
    tot = 0
    for comp in compartments:
        common_char = list(set(comp[0]).intersection(comp[1]))[0]
       
        if common_char.islower():
            tot += ord(common_char) - 96
        
        else:
            tot += ord(common_char) - 38
    
    print(tot)


for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)