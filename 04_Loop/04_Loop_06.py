n = int(input())
ans = ''

for i in range(n - 1):
    ans += ' '

ans += '*\n'

for i in range(1, n - 1):
    for j in range(n - i - 1):
        ans += ' '
    ans += '*'
    for j in range(2 * i - 1):
        ans += ' '
    ans += '*\n'

for i in range((n * 2) - 1):
    ans += '*'

print(ans)
