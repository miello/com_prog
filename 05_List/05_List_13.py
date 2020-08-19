n = int(input().strip())
l = 1
ans = []

for i in range(n):
    p = int(input().strip())
    if l:
        ans.append(p)
    else:
        ans = [p] + ans
    l ^= 1

for i in input().strip().split():
    if l:
        ans.append(int(i))
    else:
        ans = [int(i)] + ans
    l ^= 1

while True:
    data = input().strip()
    if data == '-1':
        break
    if l:
        ans.append(int(data))
    else:
        ans = [int(data)] + ans
    l ^= 1

print(ans)
