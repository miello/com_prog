def cmp(p):
    return p[0]


n = int(input())

temp_dist = []
temp = []

for p in range(n):
    a, b = [float(e) for e in input().split()]
    dist = a ** 2 + b ** 2
    temp_dist.append((dist, p + 1))
    temp.append((a, b))

temp_dist.sort(key=cmp)

idx = temp_dist[2][1]

print('#{}: {}'.format(idx, temp[idx - 1]))
