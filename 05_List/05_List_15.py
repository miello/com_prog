p = [int(e) for e in input().split()]
p.sort()
prev = p[0]
ans = []

for data in p:
    if data != prev:
        ans.append(prev)
        prev = data

ans.append(prev)

print(len(ans))
print(ans[0:10])
