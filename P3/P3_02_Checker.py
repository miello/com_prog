def helper(a, b):
    row_fail = False
    column_fail = False

    x = a.lower()
    y = b
    l = None

    if not 'a' <= x <= 'z' or len(x) > 1:
        row_fail = True
    else:
        x = ord(x) - ord('a')

    try:
        l = int(y)
        if not 1 <= l <= 52:
            raise Exception
    except:
        column_fail = True

    if row_fail and column_fail:
        print('Invalid row and column')
    elif row_fail:
        print('Invalid row')
    elif column_fail:
        print('Invalid column')
    else:
        if (x + l) % 2:
            print('White')
        else:
            print('Black')


query = input().strip()

if len(query) <= 3:
    helper(query[0], query[1:])
else:
    temp = [e.strip() for e in query.split(',')]

    if temp[0][0:3] == 'row':
        a = 0
        b = 1

    if temp[0][0:3] == 'col':
        a = 1
        b = 0

    idx_x = temp[a].find('=')
    idx_y = temp[b].find('=')

    x = ''.join(temp[a][idx_x + 1: len(temp[a])]).strip()
    y = ''.join(temp[b][idx_y + 1: len(temp[b])]).strip()

    helper(x, y)
