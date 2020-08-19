n = input()

prev = n[0]
co = 0
ans = ""

for ch in n:
    if prev == ch:
        co += 1
    else:
        ans += '{} {} '.format(prev, co)
        prev = ch
        co = 1

ans += '{} {} '.format(prev, co)
print(ans)
