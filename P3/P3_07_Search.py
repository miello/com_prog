n = int(input())

file_data = dict()

for i in range(n):
    file_name = input().strip()
    data = input().split()

    file_data[file_name] = dict()

    for j in data:
        if not file_data[file_name].get(j):
            file_data[file_name][j] = 0
        file_data[file_name][j] += 1

while True:
    word = input().strip()
    if word == '-1':
        break

    mx = 0.0
    ans = ''

    for name, value in file_data.items():
        frequent = 0.0
        if value.get(word):
            frequent = value[word] / sum(value.values())

        specific = 1 / len(value.keys())
        c = frequent * specific

        if c > mx:
            mx = c
            ans = name

    if mx == 0:
        print('NOT FOUND')
    else:
        print(ans)
