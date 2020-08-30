def compare(t_x, t_y):
    x = t_x.split()[0]
    y = t_y.split()[0]
    if int(x[-2:]) < int(y[-2:]):
        return True
    elif int(x[-2:]) > int(y[-2:]):
        return False
    return int(x) < int(y)


file_name_1, file_name_2 = input().split()

open_1 = open(file_name_1, 'r')
open_2 = open(file_name_2, 'r')

file_1 = open_1.read().splitlines()
file_2 = open_2.read().splitlines()

sz_1 = len(file_1)
sz_2 = len(file_2)
i = 0
j = 0

while i < sz_1 and j < sz_2:
    if compare(file_1[i], file_2[j]):
        print(file_1[i])
        i += 1
    else:
        print(file_2[j])
        j += 1

while i < sz_1:
    print(file_1[i])
    i += 1

while j < sz_2:
    print(file_2[j])
    j += 1

open_1.close()
open_2.close()
