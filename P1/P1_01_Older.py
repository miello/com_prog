month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

p = input().split()
p[2] = int(p[2].strip(','))
p[3] = int(p[3])
q = input().split()
q[3] = int(q[3])
q[2] = int(q[2].strip(','))

if p[3] > q[3]:
    print(q[0])
elif p[3] < q[3]:
    print(p[0])
else:
    p_idx = month.index(p[1])
    q_idx = month.index(q[1])
    if p_idx > q_idx:
        print(q[0])
    elif p_idx < q_idx:
        print(p[0])
    else:
        if p[2] > q[2]:
            print(q[0])
        elif p[2] < q[2]:
            print(p[0])
        else:
            print(p[0], q[0])
