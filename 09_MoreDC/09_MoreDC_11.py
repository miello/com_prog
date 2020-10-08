n = int(input())

for x in range(n):
    temp_str = input()
    cnt = 0
    for q in temp_str:
        if q != '.':
            break
        cnt += 1
    print('.' * (cnt // 2) + temp_str[cnt:])
