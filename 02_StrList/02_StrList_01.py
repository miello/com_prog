num = input()
now = 13
last_digit = 0

for ch in num:
    last_digit += now * (int(ch))
    last_digit %= 11
    now -= 1

last_digit = (11 - last_digit) % 10

ans = '{} {} {} {} {}'.format(num[0], num[1:5], num[5:10], num[10:12], last_digit)
print(ans)
