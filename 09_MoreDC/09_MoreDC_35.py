n = int(input())
student_info = []

for i in range(n):
    p = input().split()
    student_info.append(p)

query = input().split()
match = []

for data in student_info:
    cnt = 0
    for attr_data in data[1:]:
        for attr in query:
            if attr_data == attr:
                cnt += 1
                break
    if cnt == len(query):
        match.append(data)

if len(match) == 0:
    print('Not Found')
    exit(0)

match.sort(key=lambda x: x[0])
for p in match:
    print('{0[0]} {0[1]} {0[2]} {0[3]}'.format(p))
