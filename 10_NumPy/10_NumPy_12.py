import numpy as np


def toCelsius(f):
    x = 5 * (f - 32) / 9
    return x


def BMI(wh):
    weight = wh[::, 0]
    height = wh[::, 1] / 100
    return weight / height ** 2


def distanceTo(p, Points):
    delta_x = Points[::, 0] - p[0]
    delta_y = Points[::, 1] - p[1]
    return (delta_x ** 2 + delta_y ** 2) ** 0.5


exec(input().strip())
