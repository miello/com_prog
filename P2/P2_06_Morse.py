file_name = input()

file_open = open(file_name, 'r')
file_line = file_open.readlines()

query_type = file_line[0].strip()
morse_data = file_line[1].strip()
map_func = dict()

if query_type == 'T2M':
    idx_1 = 0

    while True:
        idx_1 = morse_data.find('[', idx_1)
        if idx_1 >= len(morse_data) - 1:
            break
        ch = morse_data[idx_1 + 1]
        idx_2 = morse_data.find(']', idx_1)
        idx_3 = morse_data.find('[', idx_2)
        map_func[ch] = morse_data[idx_2 + 1: idx_3]
        idx_1 = idx_3

    for ch in file_line[2:]:
        invalid = False
        query_data = ch.strip()
        translate_data = []

        for p in query_data:
            if not map_func.get(p):
                print('Invalid : {}'.format(query_data))
                invalid = True
                break
            translate_data.append(map_func[p])

        if not invalid:
            print(' '.join(translate_data))

elif query_type == 'M2T':
    idx_1 = 0

    while True:
        idx_1 = morse_data.find('[', idx_1)
        if idx_1 >= len(morse_data) - 1:
            break
        ch = morse_data[idx_1 + 1]
        idx_2 = morse_data.find(']', idx_1)
        idx_3 = morse_data.find('[', idx_2)
        map_func[''.join(morse_data[idx_2 + 1: idx_3])] = ch
        idx_1 = idx_3

    for ch in file_line[2:]:
        query_data = ch.strip().split()
        translate_data = []
        invalid = False

        for p in query_data:
            if not map_func.get(p):
                print('Invalid : {}'.format(' '.join(query_data)))
                invalid = True
                break
            translate_data.append(map_func[p])

        if not invalid:
            print(''.join(translate_data))

else:
    print('Invalid code')
