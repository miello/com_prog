import math

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d1, m1, y1, d2, m2, y2 = [int(e) for e in input().split()]

m1 -= 1
m2 -= 1
y1 -= 543
y2 -= 543

diff = 365 * (max(y2 - y1 - 1, 0))

if y1 % 400 == 0:
    month[1] = 29
elif y1 % 4 == 0 and y1 % 100:
    month[1] = 29

diff += month[m1] - d1 + 1

for p in range(m1 + 1, 12):
    diff += month[p]

month[1] = 28

if y2 % 400 == 0:
    month[1] = 29
elif y2 % 4 == 0 and y2 % 100:
    month[1] = 29

diff += d2 - 1

for p in range(0, m2):
    diff += month[p]

val = 2 * math.pi * diff

physical = math.sin(val / 23)
emotional = math.sin(val / 28)
interllectual = math.sin(val / 33)

print('{} {:.2f} {:.2f} {:.2f}'.format(diff, physical, emotional, interllectual))
