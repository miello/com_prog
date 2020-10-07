month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
order = {'E': 1, 'Q': 3, 'N': 7, 'F': 14}
order_list = []

while True:
    temp = input()
    if temp == 'END':
        break
    data = temp.split()
    year = int(data[4]) - 543

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        month[1] = 29
    year += 543

    if int(data[4]) < 2558:
        print('Error: ' + temp + ' --> Invalid year')
    elif not 1 <= int(data[3]) <= 12:
        print('Error: ' + temp + ' --> Invalid month')
    elif not 1 <= int(data[2]) <= month[int(data[3]) - 1]:
        print('Error: ' + temp + ' --> Invalid date')
    elif data[1] not in list(order.keys()):
        print('Error: ' + temp + ' --> Invalid delivery type')
    else:
        new_day = int(data[2]) + order[data[1]]
        month_data = int(data[3]) - 1
        if new_day > month[month_data]:
            new_day -= month[month_data]
            month_data += 1
        if month_data == 12:
            month_data -= 12
            year += 1
        order_list.append((data[0], new_day, month_data + 1, year))

    month[1] = 28

order_list.sort(key=lambda x: (x[3], x[2], x[1], int(x[0])))

for x in order_list:
    print('{}: delivered on {}/{}/{}'.format(x[0], x[1], x[2], x[3]))
