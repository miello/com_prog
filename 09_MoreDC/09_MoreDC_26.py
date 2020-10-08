n = int(input())
database = dict()
list_id = []

for i in range(n):
    _id, temp = input().split(': ')
    history = set(temp.split(', '))

    if database.get(_id) == None:
        database[_id] = set()

    for p in history:
        database[_id].add(p)
    list_id.append(_id)

t = input()
query_data = database[t]
found = False

for idx in list_id:
    data = database[idx]
    if idx != t:
        if len(query_data & data) != 0:
            found = True
            print(idx)

if not found:
    print('Not Found')
