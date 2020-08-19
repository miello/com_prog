n = int(input())
ans = []

while n != 1:
    ans.append(str(n))
    if n & 1:
        n = 3 * n + 1
    else:
        n //= 2

ans.append('1')
print('->'.join(ans[-15:]))
