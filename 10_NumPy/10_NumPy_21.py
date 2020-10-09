import numpy as np


def sum_2_rows(M):
    row = M.shape[0]
    return np.array([M[e] + M[e + 1] for e in range(0, row, 2)])


def sum_left_right(M):
    column = M.shape[1]
    p = M[:, 0:column // 2] + M[:, column // 2: column]
    return p


def sum_upper_lower(M):
    row = M.shape[0]
    p = M[0:row // 2, :] + M[row // 2: row, :]
    return p


def sum_4_quadrants(M):
    row = M.shape[0]
    column = M.shape[1]
    p = M[0: row // 2, 0: column // 2] + M[0: row // 2, column // 2: column]
    p += M[row // 2: row, 0: column // 2] + M[row // 2: row, column // 2: column]
    return p


def sum_4_cells(M):
    p = M.shape[0]
    ans = np.zeros((p // 2, p // 2), int)
    for l in range(0, p, 2):
        for q in range(0, p, 2):
            ans[l // 2][q // 2] = sum(sum(M[l: l + 2, q: q + 2]))
    return ans


def count_leap_years(years):
    years = years - 543
    return years[(years % 400 == 0) | ((years % 4 == 0) & (years % 100 != 0))].shape[0]


exec(input().strip())
