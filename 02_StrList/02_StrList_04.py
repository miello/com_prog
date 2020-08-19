m = input().strip()
n = int(input().strip())

ans = '0' * (max(n - len(m), 0)) + m

print(ans)
