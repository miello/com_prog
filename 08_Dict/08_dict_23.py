n = int(input())

tel_to_name = dict()
name_to_tel = dict()

for i in range(n):
    p = input().split()
    tel = p[2]
    name = ' '.join(p[0:2])
    name_to_tel[name] = tel
    tel_to_name[tel] = name

m = int(input())

for i in range(m):
    p = input().strip()
    print('{} --> '.format(p), end='')
    if tel_to_name.get(p):
        print('{}'.format(tel_to_name[p]))
    elif name_to_tel.get(p):
        print('{}'.format(name_to_tel[p]))
    else:
        print('Not found')
