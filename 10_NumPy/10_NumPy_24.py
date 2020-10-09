import numpy as np


def peak_indexes(x):
    temp = x[1: -1]
    idx = np.arange(1, len(x) - 1, 1)

    ans = idx[(x[0: -2] < temp) & (x[2:] < temp)]

    return ans


def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")


exec(input().strip())
