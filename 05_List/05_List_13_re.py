n = int(input())

ans = []
temp = []

for p in range(n):
    l = int(input().strip())
    temp.append(l)

ans += temp

inp = input().strip().split()
ans += [int(e) for e in inp]

temp = []

while True:
    l = input().strip()
    if l == '-1':
        break
    temp.append(int(l))

ans += temp
ans_2 = []
l = 0
st = None

if len(ans) & 1:
    st = len(ans) - 2
else:
    st = len(ans) - 1

for data in range(st, -1, -2):
    ans_2.append(ans[data])
    l = data

l ^= 1

for data in range(l, len(ans), 2):
    ans_2.append(ans[data])

print(ans_2)
