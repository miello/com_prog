deg = input().strip()
n = int(input().strip())
sz = 0
x = []

for p in range(n):
    l = input().strip()
    if sz == 0:
        sz = len(l)
    elif sz != len(l):
        print('Invalid size')
        exit()
    x.append(list(l))

if deg == 'flip':
    for data in x:
        print("".join(data[::-1]))
elif deg == '90':
    for i in range(len(x[0])):
        for j in range(len(x) - 1, -1, -1):
            print('{}'.format(x[j][i]), sep="", end="")
        print()
elif deg == '180':
    x = x[::-1]
    for data in x:
        print("".join(data[::-1]))
