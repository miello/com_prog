def convert(abbre, p, val):
    digit_divide = 10 ** (p - 2)
    case_pow = 10 ** (p - 1)
    pow = 10 ** (p)
    if 0 <= sub_int // pow <= 9:
        ans = sub_int // case_pow
        fdigit = sub_int // digit_divide
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}.{}{}'.format(ans // 10, ans % 10, abbre))
    else:
        ans = sub_int // pow
        fdigit = sub_int // case_pow
        ans += 1 * int(fdigit % 10 >= 5)
        print('{}{}'.format(ans, abbre))


sub = input().strip()

sub_int = int(sub)
digit = len(sub) - 1
pow = 0

if digit < 3:
    print(sub_int)

elif digit < 6:
    convert('K', 3, sub_int)

elif digit < 9:
    convert('M', 6, sub_int)

else:
    convert('B', 9, sub_int)
