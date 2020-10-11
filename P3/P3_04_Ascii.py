file_data = [e.strip() for e in open(input(), 'r').readlines()]

final_list = ['' for e in range(len(file_data))]


query = input()
len_text = len(file_data[0])
len_line = len(file_data)

if query == 'LSTRIP':
    bound = False
    r = 0
    for p in range(len_text):
        for q in range(len_line):
            if file_data[q][p] != '.':
                r = p
                bound = True
                break
        if bound:
            break
    for p in file_data:
        print(p[r:])

elif query == 'RSTRIP':
    bound = False
    r = 0
    for p in range(len_text - 1, -1, -1):
        for q in range(len_line):
            if file_data[q][p] != '.':
                r = p
                bound = True
                break
        if bound:
            break
    for p in file_data:
        print(p[:r + 1])
    pass
elif query == 'STRIP':
    bound = False
    r = 0
    for p in range(len_text - 1, -1, -1):
        for q in range(len_line):
            if file_data[q][p] != '.':
                r = p
                bound = True
                break
        if bound:
            break
    bound = False
    l = 0
    for p in range(len_text):
        for q in range(len_line):
            if file_data[q][p] != '.':
                l = p
                bound = True
                break
        if bound:
            break
    for p in file_data:
        print(p[l:r + 1])
    pass
elif query == 'STRIP_ALL':
    list_remove = []
    for p in range(len_text):
        bound = False
        for q in range(len_line):
            if file_data[q][p] != '.':
                bound = True
                break
        if not bound:
            list_remove.append(p)
    for p in range(len_line):
        idx_now = 0
        for q in range(len_text):
            if idx_now < len(list_remove):
                if q == list_remove[idx_now]:
                    idx_now += 1
                else:
                    print(file_data[p][q], end='')
        print()
else:
    print('Invalid command')
