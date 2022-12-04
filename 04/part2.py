from utils import *

sample1 = r"""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

sample2 = r""""""

actual_input = read_input()


def run_on_input(ipt):
    pairs = [r.split(",") for r in ipt.split("\n")]
    int_pairs = [[[int(x) for x in s.split("-")] for s in p] for p in pairs]
    
    overlaps = 0
    for pair in int_pairs:
        a1, a2 = pair[0]
        b1, b2 = pair[1]
        a = set(range(a1, a2 + 1))
        b = set(range(b1, b2 + 1))
        shared = a.intersection(b)
        overlaps += len(shared) > 0

    print(overlaps)



for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)