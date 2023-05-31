from utils import *
import numpy as np


sample1 = r"""30373
25512
65332
33549
35390"""
sample2 = r""""""
sample3 = r""""""

actual_input = read_input()


def run_on_input(ipt):
    tree_grid = ipt.splitlines()
    n_rows = len(tree_grid)
    n_cols = len(tree_grid[0])
    scenic_score = np.ones((n_rows, n_cols))

    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            tree_height = int(tree_grid[i][j])
            left_neighbours  = [(i, col_idx) for col_idx in range(0, j)][::-1]
            right_neighbours = [(i, col_idx) for col_idx in range(j + 1, n_cols)]
            up_neighbours    = [(row_idx, j) for row_idx in range(0, i)][::-1]
            down_neighbours  = [(row_idx, j) for row_idx in range(i + 1, n_rows)]

            for neighbours in [left_neighbours, right_neighbours, up_neighbours, down_neighbours]:
                for view_dist, (ni, nj) in enumerate(neighbours):
                    if int(tree_grid[ni][nj]) >= tree_height:
                        break

                scenic_score[i, j] = scenic_score[i, j] * (view_dist + 1)

    print(np.max(scenic_score, axis=(0, 1)))


for ipt in [sample1, sample2, sample3, actual_input]:
    if ipt:
        run_on_input(ipt)
