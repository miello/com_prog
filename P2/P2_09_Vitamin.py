n = int(input())

fruit = []

for i in range(n):
    temp = input().split()
    for j in range(1, len(temp)):
        temp[j] = float(temp[j])
    fruit.append(temp)

query = input().split()
if query[0] == 'show':
    for p in fruit:
        for l in p:
            print('{} '.format(l), end='')
        print()
elif query[0] == 'get':
    for p in fruit:
        found = False
        if p[0] == query[1]:
            for q in p:
                print('{} '.format(q), end='')
            print()
            found = True
            break
    if not found:
        print('{} not found'.format(query[1]))
elif query[0] == 'avg':
    sum_avg = 0
    idx = int(query[1])
    for p in fruit:
        sum_avg += p[idx]
    sum_avg /= n
    print(round(sum_avg, 4))
elif query[0] == 'max':
    idx = int(query[1])
    fruit.sort(key=lambda x: (-x[idx], x[0]))
    print(fruit[0][0], fruit[0][idx])
elif query[0] == 'sort':
    idx = int(query[1])
    fruit.sort(key=lambda x: (x[idx], x[0]))
    for p in fruit:
        print('{} '.format(p[0]), end='')
