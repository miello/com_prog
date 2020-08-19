n = float(input().strip())

l = 0
u = n
x = (l + u) / 2

while abs(n - 10 ** x) > (10 ** (-10)) * max(n, 10 ** x):
    if 10 ** x > n:
        u = x
    if 10 ** x < n:
        l = x
    x = (l + u) / 2

print(round(x, 6))
