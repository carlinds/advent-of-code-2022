from utils import *


sample1 = r"""mjqjpqmgbljsphdztnvjfqwrcgsmlb"""
sample2 = r"""bvwbjplbgvbhsrlpgdmjqwftvncz"""
sample3 = r"""nppdvjthqldpwncqszvftbrmjlhg"""

actual_input = read_input()

def run_on_input(ipt):
    buffer_length = 14
    buffer = []
    for sequence_start in range(len(ipt)):
        for buffer_idx in range(buffer_length):
            idx = sequence_start + buffer_idx
            if ipt[idx] not in buffer:
                buffer.append(ipt[idx])
            else:
                buffer = []
                break
        if len(buffer) == buffer_length:
            break

    print(idx+1)
        

for ipt in [sample1, sample2, sample3, actual_input]:
    if ipt:
        run_on_input(ipt)