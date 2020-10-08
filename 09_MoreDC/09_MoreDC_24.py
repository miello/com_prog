collection = dict()
list_type = []

while True:
    temp = input().strip()
    if temp == 'q':
        break
    name, _type = temp.split(', ')
    if not collection.get(_type):
        collection[_type] = []
        list_type.append(_type)
    collection[_type].append(name)

for p in list_type:
    data = collection[p]
    temp_list = ', '.join(data)
    print('{}: {}'.format(p, temp_list))
