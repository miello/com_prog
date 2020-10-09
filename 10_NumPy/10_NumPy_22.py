import numpy as np


def mult_table(nrows, ncols):
    base = np.arange(1, nrows + 1, 1)
    base.resize((nrows, 1))

    mul = np.arange(1, ncols + 1, 1)
    return base * mul


exec(input().strip())
