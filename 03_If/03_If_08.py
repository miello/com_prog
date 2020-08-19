month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = int(input().strip())
m = int(input().strip())
y = int(input().strip())

y -= 543
m -= 1

if y % 400 == 0 or (y % 4 == 0 and y % 100):
    month[1] = 29

day = sum(day[0:m]) + d

# for i in range(12):
#     if i == m:
#         day += d
#         break
#     day += month[i]

print(day)
