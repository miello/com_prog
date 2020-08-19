number = input()

if len(number) != 10 or number[0] != '0':
    print('Not a mobile number')
elif number[0] == '0':
    ch = number[1]
    if ch == '6' or ch == '8' or ch == '9':
        print('Mobile number')
    else:
        print('Not a mobile number')
