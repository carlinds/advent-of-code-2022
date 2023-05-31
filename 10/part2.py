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
sample2 = r"""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""
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

def plot_knots(knots, start_point):
    plt.figure()
    #plt.plot([p[1] for p in knots[0].visited], [p[0] for p in knots[0].visited], "-o", label="Head")
    for i, knot in enumerate(knots[::-1]):
        plt.plot(knot.visited[-1][1], knot.visited[-1][0], "o", label=len(knots)-i-1    )
        #plt.plot([p[1] for p in knot.visited[-1]], [p[0] for p in knot.visited[-1]], "-o", label=i)
    
    plt.plot(start_point[1], start_point[0], "o", label="Start")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()


def run_on_input(ipt):
    lines = ipt.splitlines()

    start_point = (0, 0)
    
    knots = [Knot(start_point) for _ in range(10)]

    for line in lines:
        head_direction, n_steps = line.split(" ")
        n_steps = int(n_steps)

        for i in range(n_steps):
            knots[0].move(head_direction)
            
            for j in range(1, 10):
                    
                if knots[j-1].dist_to_knot(knots[j]) < 2:
                    continue

                elif knots[j-1].pos[0] == knots[j].pos[0] and knots[j-1].pos[1] < knots[j].pos[1]:
                    knots[j].move("L")

                elif knots[j-1].pos[0] == knots[j].pos[0] and knots[j-1].pos[1] > knots[j].pos[1]:
                    knots[j].move("R")

                elif knots[j-1].pos[0] > knots[j].pos[0] and knots[j-1].pos[1] == knots[j].pos[1]:
                    knots[j].move("D")

                elif knots[j-1].pos[0] < knots[j].pos[0] and knots[j-1].pos[1] == knots[j].pos[1]:
                    knots[j].move("U")

                elif knots[j].pos[0] < knots[j-1].pos[0] and knots[j].pos[1] < knots[j-1].pos[1]:
                    knots[j].move("RD")

                elif knots[j].pos[0] < knots[j-1].pos[0] and knots[j].pos[1] > knots[j-1].pos[1]:
                    knots[j].move("LD")

                elif knots[j].pos[0] > knots[j-1].pos[0] and knots[j].pos[1] > knots[j-1].pos[1]:
                    knots[j].move("LU")

                elif knots[j].pos[0] > knots[j-1].pos[0] and knots[j].pos[1] < knots[j-1].pos[1]:
                    knots[j].move("RU")

                #plot_knots(knots, start_point)


    print(len(set(knots[-1].visited)))
    plt.figure()
    #plt.plot([p[1] for p in knots[0].visited], [p[0] for p in knots[0].visited], "-o", label="Head")
    plt.plot([p[1] for p in knots[-1].visited], [p[0] for p in knots[-1].visited], "-o", label="Tail")
    plt.plot(start_point[1], start_point[0], "o", label="Start")
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()


for ipt in [sample1, sample2, sample3, actual_input]:
#for ipt in [sample2]:
    if ipt:
        run_on_input(ipt)
