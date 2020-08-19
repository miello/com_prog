import math

pi = math.pi
e = math.e

n = int(input())

c = (math.sqrt(2 * pi) * (n ** (n + (1 / 2))))
upper = c * (e ** (-n + (1 / (12 * n))))
lower = c * (e ** (-n + (1 / (12 * n + 1))))
print(lower)
print(upper)
