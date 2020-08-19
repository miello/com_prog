l = input()

p = [False] * 10
ans = []

for ch in l:
    if '0' <= ch <= '9':
        p[int(ch)] = True

for ch in range(10):
    if not p[ch]:
        ans.append(str(ch))

if len(ans) == 0:
    print('None')
else:
    print(",".join(ans))
