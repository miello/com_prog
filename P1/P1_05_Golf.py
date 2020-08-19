import math

par_sum = 0
stroke_sum = 0
edit_sum = 0

for i in range(9):
    x, y, z = [int(e) for e in input().strip().split()]
    par_sum += x
    stroke_sum += y
    if z == 1:
        edit_sum += min(x + 2, y)

cal_edit = math.floor(0.8 * ((1.5 * edit_sum) - par_sum))
score = stroke_sum - cal_edit

print(stroke_sum)
print(cal_edit)
print(score)
