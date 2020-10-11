file_open = open(input(), 'r').readlines()

file_data = '.'.join([e.strip() for e in file_open])

k = int(input())

for p in range(1, k + 1):
    if p % 10 == 0:
        print(str(p // 10), end='')
    else:
        print('-', end='')

print()

word_set = []

prev = file_data[0]
cnt_dot = 0

file_data = file_data.strip('.')
temp_word_set = []

for p in file_data:
    if p == '.':
        if len(temp_word_set) != 0:
            word_set.append(temp_word_set)
            temp_word_set = []
        cnt_dot += 1
    else:
        if cnt_dot != 0:
            word_set.append(['.'] * cnt_dot)
            cnt_dot = 0
        temp_word_set.append(p)

word_set.append(temp_word_set)
line = []

cnt = 0
idx = 0

temp_line = []

while idx < len(word_set):
    if len(word_set[idx]) > k:
        if len(temp_line) > 0:
            line.append(temp_line)
            temp_line = []
            cnt = 0
        line.append(word_set[idx])
        idx += 1
    elif cnt + len(word_set[idx]) <= k:
        cnt += len(word_set[idx])
        temp_line.append(word_set[idx])
        idx += 1
    else:
        line.append(temp_line)
        if word_set[idx][0] == '.':
            idx += 1
        cnt = 0
        temp_line = []

if len(temp_line) != 0:
    line.append(temp_line)

for p in line:
    temp = []
    for q in p:
        for text in q:
            temp.append(text)
    temp = ''.join(temp)
    print(temp.strip('.'))
