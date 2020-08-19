n = int(input())
command = None
zig_1 = None
zag_1 = None
zig_2 = None
zag_2 = None
tick = 0

while True:
    p = input().split()
    if p[0] == 'Zig-Zag' or p[0] == 'Zag-Zig':
        command = p[0]
        break
    fv = int(p[0])
    sv = int(p[1])
    if tick == 0:
        zig_1 = fv
        zag_1 = sv
        zig_2 = fv
        zag_2 = sv
    elif tick & 1 == 0:
        zig_1 = min(zig_1, fv)
        zag_1 = max(zag_1, sv)
        zig_2 = max(zig_2, fv)
        zag_2 = min(zag_2, sv)
    else:
        zig_1 = min(zig_1, sv)
        zag_1 = max(zag_1, fv)
        zig_2 = max(zig_2, sv)
        zag_2 = min(zag_2, fv)
    tick += 1

if command == 'Zig-Zag':
    print(zig_1, zag_1)
else:
    print(zag_2, zig_2)
