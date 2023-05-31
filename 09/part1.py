from utils import *
import numpy as np
import math
import matplotlib.pyplot as plt

sample1 = r"""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
sample2 = r""""""
sample3 = r""""""

actual_input = read_input()

class Knot():
    def __init__(self, init_pos):
        self.pos = init_pos
        self.visited = [self.pos]

    def move(self, command):
        match command:
            case "R":
                self.pos = (self.pos[0], self.pos[1] + 1)

            case "L":
                self.pos = (self.pos[0], self.pos[1] - 1)
                
            case "U":
                self.pos = (self.pos[0] -1, self.pos[1])

            case "D":
                self.pos = (self.pos[0] + 1, self.pos[1])

            case "RU":
                self.pos = (self.pos[0] - 1, self.pos[1] + 1)

            case "LU":
                self.pos = (self.pos[0] - 1, self.pos[1] - 1)

            case "RD":
                self.pos = (self.pos[0] + 1, self.pos[1] + 1)
                
            case "LD":
                self.pos = (self.pos[0] + 1, self.pos[1] - 1)
                
        self.visited.append(self.pos)

    def dist_to_knot(self, other_knot):
        return math.sqrt((self.pos[0] - other_knot.pos[0])**2 + (self.pos[1] - other_knot.pos[1])**2)

def run_on_input(ipt):
    lines = ipt.splitlines()

    start_point = (0, 0)
    head = Knot(start_point)
    tail = Knot(start_point)

    for line in lines:
        head_direction, n_steps = line.split(" ")
        n_steps = int(n_steps)

        for i in range(n_steps):
            head.move(head_direction)
            
            if head.dist_to_knot(tail) < 2:
                continue

            if head.pos[0] == tail.pos[0] or head.pos[1] == tail.pos[1]:
                tail.move(head_direction)

            elif tail.pos[0] < head.pos[0] and tail.pos[1] < head.pos[1]:
                tail.move("RD")

            elif tail.pos[0] < head.pos[0] and tail.pos[1] > head.pos[1]:
                tail.move("LD")

            elif tail.pos[0] > head.pos[0] and tail.pos[1] > head.pos[1]:
                tail.move("LU")

            elif tail.pos[0] > head.pos[0] and tail.pos[1] < head.pos[1]:
                tail.move("RU")

    print(len(set(tail.visited)))
    plt.figure()
    plt.plot([p[1] for p in head.visited], [p[0] for p in head.visited], "-o", label="Head")
    plt.plot([p[1] for p in tail.visited], [p[0] for p in tail.visited], "-o", label="Tail")
    plt.plot(start_point[1], start_point[0], "o", label="Start")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()


for ipt in [sample1, sample2, sample3, actual_input]:
    if ipt:
        run_on_input(ipt)
