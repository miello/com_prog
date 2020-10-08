n = int(input())

time_dict = dict()

for i in range(n):
    q = input().split(', ')
    minute, second = [int(e) for e in q[3].split(':')]
    if not time_dict.get(q[2]):
        time_dict[q[2]] = [0, 0]
    time_dict[q[2]] = [time_dict[q[2]][0] + minute, time_dict[q[2]][1] + second]

convert_time = time_dict.values()

for p in convert_time:
    temp = p[1] // 60
    p[1] %= 60
    p[0] += temp

list_time = list(time_dict.items())

list_time.sort(key=lambda x: (x[1][0], x[1][1]), reverse=True)

for e in range(0, min(3, len(list_time))):
    print('{} --> {}:{:02d}'.format(list_time[e][0], list_time[e][1][0], list_time[e][1][1]))
