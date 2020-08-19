data = input().strip().split()
tar = input().strip()

ans = data[:]
l = len(ans)
l //= 2

for ch in tar:
    if ch == 'C':
        ans = ans[l:] + ans[0: l]
    elif ch == 'S':
        temp = []
        pos_1 = 0
        pos_2 = l
        now = 0
        while pos_1 < l and pos_2 < len(ans):
            if not now:
                temp.append(ans[pos_1])
                pos_1 += 1
            else:
                temp.append(ans[pos_2])
                pos_2 += 1
            now ^= 1
        if pos_1 < l:
            temp.append(ans[pos_1])
        if pos_2 < len(ans):
            temp.append(ans[pos_2])
        ans = temp[:]

print(" ".join(ans))
