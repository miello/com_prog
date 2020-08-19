command = input().strip()

if command == 'str2RLE':
    l = input()
    prev = l[0]
    co = 0
    ans = ""
    for data in l:
        if prev == data:
            co += 1
        else:
            ans += '{} {} '.format(prev, co)
            co = 1
            prev = data

    ans += '{} {} '.format(prev, co)
    print(ans)
elif command == 'RLE2str':
    l = input()
    l = l.split()
    ans = []
    for i in range(0, len(l), 2):
        text = l[i]
        num = int(l[i + 1])
        for j in range(num):
            ans.append(text)
    print("".join(ans))
else:
    print('Error')
