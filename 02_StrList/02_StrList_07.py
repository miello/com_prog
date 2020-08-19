n = list(input())
step_1 = ""
step_2 = ""

for e in range(3, 32, 7):
    step_1 += str(n[e])

for e in range(7, 32, 5):
    step_2 += str(n[e])

step_3 = int(step_1) + int(step_2) + 10000
step_4 = (step_3 % 10000) - (step_3 % 10)
ans_1 = str(step_4 // 10)
ans_2 = 0
co = 0

while step_4 != 0:
    ans_2 += step_4 % 10
    co += 1
    step_4 //= 10

ans_1 = '0' * (max(0, 3 - len(ans_1))) + ans_1
ans_2 = ((ans_2) % 10)

print('{}{}'.format(ans_1, chr(65 + ans_2)))
