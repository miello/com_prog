n = int(input())
p = []
start = None
now = None
t = None
sum = 0
idx = 0
co = 0

for i in range(n):
    l = input().strip().split()
    if l[0] == 'reset':
        num = int(l[1])
        now = num

    elif l[0] == 'new':
        num = int(l[1])
        if t == None:
            t = num
        p.append((now, num))
        print('ticket {}'.format(now))
        now += 1

    elif l[0] == 'next':
        print('call {}'.format(p[idx][0]))
        idx += 1

    elif l[0] == 'order':
        num = int(l[1])
        sum += num - p[idx - 1][1]
        print('qtime {} {}'.format(p[idx - 1][0], num - p[idx - 1][1]))
        co += 1

    elif l[0] == 'avg_qtime':
        avg = round(sum / co, 4)
        print('avg_qtime {}'.format(avg))
