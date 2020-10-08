course_IO = open(input(), 'r')
teacher_IO = open(input(), 'r')
database_IO = open(input(), 'r')

course_dict = dict()
teacher_dict = dict()

for p in course_IO.readlines():
    p = p.strip().split(',')
    course_dict[p[0]] = p[1]

for p in teacher_IO.readlines():
    p = p.strip().split(',')
    teacher_dict[p[0]] = p[1]

for p in database_IO.readlines():
    p = p.strip().split(',')
    if not course_dict.get(p[0]) or not teacher_dict.get(p[1]):
        print('record error')
        continue
    print('{},{}'.format(course_dict[p[0]], teacher_dict[p[1]]))
