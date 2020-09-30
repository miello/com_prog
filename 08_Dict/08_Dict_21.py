p = input().strip().lower()
cnt = dict()

for ch in p:
    if not 'a' <= ch <= 'z':
        continue
    if not cnt.get(ch):
        cnt[ch] = 0
    cnt[ch] += 1

temp = list(cnt.items())

temp.sort(key=lambda x: (x[1] * -1, x[0]))

for key, val in temp:
    print('{} -> {}'.format(key, val))
