import numpy as np


def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data


def report_lower_than_mean(weight, data):
    store = sum((weight * data[:, 1:]).T)
    mean = sum(store) / data.shape[0]
    lower = data[store < mean]

    if len(lower) == 0:
        print(None)
        return

    ans = [str(e) for e in lower[:, 0]]
    print(', '.join(ans))


exec(input().strip())
