l = [float(e) for e in input().split()]

ans_sum = 0
ans_min, ans_max = l[0], l[0]

for data in l:
    ans_sum += data
    if ans_min >= data:
        ans_min = data
    if ans_max <= data:
        ans_max = data

ans = (ans_sum - ans_min - ans_max) / 2

print(round(ans, 2))
