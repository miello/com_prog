n = int(input())
k = int(input())

if n < 1 and k < 1:
    print('Invalid n and k')
elif n < 1:
    print('Invalid n')
elif k < 1:
    print('Invalid k')
else:
    for l in range(1, k + 1):
        temp = n
        if l >= 10:
            temp -= 1
        if l >= 100:
            temp -= 1
        if l == k:
            temp -= 1
        print('{}'.format(l) + '-' * temp, end='')
    print()
    one_bit = ['0', '1']
    while n > 1:
        back = ['0' + e for e in one_bit]
        front = ['1' + e for e in one_bit[::-1]]
        one_bit = back + front
        n -= 1
    cnt = 0
    for p in one_bit:
        print(p, end='')
        cnt += 1
        if cnt == k:
            print()
            cnt = 0
        else:
            if one_bit[-1] != p:
                print(',', end='')
