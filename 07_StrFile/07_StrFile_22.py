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

if p != q:
    print('NO')
else:
    print('YES')
