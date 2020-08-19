val = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
id = []
grade = []
ans = []


def cmp(p):
    return p[0]


while True:
    p = input().strip()
    if p == 'q':
        break
    p = p.split()
    id.append(p[0])
    grade.append(val.index(p[1]))

for q in input().strip().split():
    pos = id.index(q)
    grade[pos] = max(0, grade[pos] - 1)

for q in range(len(id)):
    ans.append((int(id[q]), grade[q]))

ans.sort(key=cmp)

for q in ans:
    print('{} {}'.format(q[0], val[q[1]]))
