import numpy as np
from math import e


def p(X):
    logit = -3.98 + 0.1 * X[::, 0] + 0.5 * X[::, 1]
    p_data = 1 / (1 + e ** (-logit))
    return p_data


exec(input().strip())
