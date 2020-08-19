a = input().strip()
a = a[1:len(a) - 1].split(',')
b = input().strip()
b = b[1:len(b) - 1].split(',')

a = [float(e) for e in a]
b = [float(e) for e in b]
ans = [a[i] + b[i] for i in range(0, len(a))]

print('{} + {} = {}'.format(a, b, ans))
