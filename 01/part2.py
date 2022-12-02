from utils import *

sample1 = r"""
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

sample2 = r""""""

actual_input = read_input()

def run_on_input(ipt):
    grps = [int_list(g) for g in ipt.split("\n\n")]
    tot_cals = [sum(l) for l in grps]
    print(sum(sorted(tot_cals, reverse=True)[:3]))

for ipt in [sample1, sample2, actual_input]:
    if ipt:
        run_on_input(ipt)