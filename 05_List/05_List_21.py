val = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
id = []
grade = []

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
    print('{} {}'.format(id[q], val[grade[q]]))
