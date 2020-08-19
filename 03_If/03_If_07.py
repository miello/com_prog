sub = input().strip()

sub_int = int(sub)
digit = len(sub) - 1
pow = 0

if digit < 3:
    print(sub_int)

elif digit < 6:
    digit_divide = 10
    case_pow = 10 ** 2
    pow = 10 ** 3
    if 0 <= sub_int // pow <= 9:
        ans = sub_int // case_pow
        fdigit = sub_int // digit_divide
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}.{}K'.format(ans // 10, ans % 10))
    else:
        ans = sub_int // pow
        fdigit = sub_int // case_pow
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}K'.format(ans))

elif digit < 9:
    digit_divide = 10 ** 4
    case_pow = 10 ** 5
    pow = 10 ** 6
    if 0 <= sub_int // pow <= 9:
        ans = sub_int // case_pow
        fdigit = sub_int // digit_divide
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}.{}M'.format(ans // 10, ans % 10))
    else:
        ans = sub_int // pow
        fdigit = sub_int // case_pow
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}M'.format(ans))

else:
    digit_divide = 10 ** 7
    case_pow = 10 ** 8
    pow = 10 ** 9
    if 0 <= sub_int // pow <= 9:
        ans = sub_int // case_pow
        fdigit = sub_int // digit_divide
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}.{}B'.format(ans // 10, ans % 10))
    else:
        ans = sub_int // pow
        fdigit = sub_int // case_pow
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}B'.format(ans))
