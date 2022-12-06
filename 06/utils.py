import numpy as np

def lmap(func, *iterables):
    return list(map(func, *iterables))

def list_diff(l):
    return np.diff(l) 

def read_input():
    return open("input.txt").read()

def int_list(ipt):
    return [int(s) for s in ipt.split()]

def float_list(ipt):
    return [float(s) for s in ipt.split()]

def string_list(ipt):
    return ipt.split()

def sliding_window(l, n):
    return np.convolve(l, np.ones(n), mode="valid")