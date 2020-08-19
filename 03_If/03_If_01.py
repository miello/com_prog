n = input().strip()

for ch in n:
    if '0' <= ch <= '9':
        continue
    else:
        print('Error')
        exit(0)

if len(n) != 2:
    print('Error')
elif n[0] == '2' or n[0] == '3':
    print('OK')
elif n[0] == '4' and n[1] == '0':
    print('OK')
elif n[0] == '0':
    if n[1] == '1' or n[1] == '2':
        print('OK')
    else:
        print('Error')
elif n[0] == '5':
    if n[1] == '1' or n[1] == '3' or n[1] == '5' or n[1] == '8':
        print('OK')
    else:
        print('Error')
else:
    print('Error')
