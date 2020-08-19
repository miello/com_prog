d = []

while True:
    p = input().strip()
    if p == 'q':
        break
    d.append(float(p))

if len(d) == 0:
    print('No Data')
else:
    ave = sum(d) / len(d)
    print(round(ave, 2))
