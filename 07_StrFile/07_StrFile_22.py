p = list("".join(input().split()))
q = list("".join(input().split()))

for idx, e in enumerate(p):
    if 'A' <= e <= 'Z':
        p[idx] = chr(ord(e) + 32)

for idx, e in enumerate(q):
    if 'A' <= e <= 'Z':
        q[idx] = chr(ord(e) + 32)

p.sort()
q.sort()

if len(p) != len(q):
    print('NO')
    exit()

for idx in range(len(p)):
    if p[idx] != q[idx]:
        print('NO')
        exit()

print('YES')
