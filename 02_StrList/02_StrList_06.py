a = list(input().strip('[]').split(', '))
b = list(input().strip('[]').split(', '))

a = [float(e) for e in a]
b = [float(e) for e in b]
ans = [a[i] + b[i] for i in range(0, len(a))]

print('{} + {} = {}'.format(a, b, ans))
