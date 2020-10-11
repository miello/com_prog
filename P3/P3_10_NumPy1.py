import numpy as np


def eq(A, B, p):
    shape = A.shape
    sz = 1

    for x in shape:
        sz *= x

    cnt = sum(A == B)

    for i in range(len(A)):
        cnt = np.sum(cnt)

    return cnt >= (sz * p) / 100


def closest_point_indexes(points, p):
    points -= p
    temp = points ** 2
    idx = np.arange(0, len(points), 1)

    temp = sum(temp.T) ** (0.5)
    mn = np.min(temp)

    return idx[temp == mn]
    pass


def number_of_inversions(A):
    sz = A.shape[0]
    cnt = 0
    for i in range(sz):
        cnt += np.sum(A[i] > A[i + 1: sz])
    return cnt


exec(input().strip())
