h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

dh = (24 + h2 - h1) % 24
dm = m2 - m1

if dm < 0:
    dh -= 1
    dm += 60
    dh = (24 + dh) % 24

ds = s2 - s1

if ds < 0:
    dm -= 1
    ds += 60
    if dm < 0:
        dm += 60
        dh -= 1
        if dh < 0:
            dh += 24

print('{}:{}:{}'.format(dh, dm, ds))
