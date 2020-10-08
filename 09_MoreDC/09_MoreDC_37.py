n = int(input())

result = []
cap = dict()

for i in range(n):
    depart, amount = input().split()
    amount = int(amount)
    cap[depart] = amount

m = int(input())
temp = []

for i in range(m):
    l = input().split()
    l[1] = float(l[1])
    temp.append(l)

temp.sort(key=lambda x: -x[1])

for p in temp:
    for q in p[2:]:
        if cap[q] != 0:
            result.append((p[0], q))
            cap[q] -= 1
            break

result.sort(key=lambda x: x[0])
for p in result:
    print('{0[0]} {0[1]}'.format(p))
