a = float(input().strip())
b = float(input().strip())
c = float(input().strip())

d = (b ** 2 - 4 * a * c) ** (1 / 2)
x1 = round(((-b - d) / (2 * a)), 3)
x2 = round(((-b + d) / (2 * a)), 3)
print('{0} {1}'.format(x1, x2))
