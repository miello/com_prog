valid_dna = 'ATGC'
reverse_comp = 'TACG'

dna = list(input().strip())
typ = input().strip()

for idx, ch in enumerate(dna):
    if 'a' <= ch <= 'z':
        dna[idx] = chr(ord(ch) - 32)
    if dna[idx] not in valid_dna:
        print('Invalid DNA')
        exit()

if typ == 'R':
    ans = ''
    for ch in dna:
        idx = valid_dna.index(ch)
        rev_comp = reverse_comp[idx]
        ans += rev_comp
    print(ans[::-1])

elif typ == 'F':
    cnt_comp = [0] * 4
    ans = []

    for ch in dna:
        cnt_comp[valid_dna.index(ch)] += 1
    for p in range(4):
        ans.append('{}={}'.format(valid_dna[p], cnt_comp[p]))

    print(", ".join(ans))

elif typ == 'D':
    tar = input().strip()
    cnt = 0

    for p in range(len(dna) - len(tar) + 1):
        str_join = "".join(dna[p:p + len(tar)])
        if str_join == tar:
            cnt += 1

    print(cnt)
