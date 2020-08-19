n = int(input())

full_name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick_name = ['Dick', 'Bill', 'Jim', 'Jack', 'Peggy', 'Ed', 'Sally', 'Andy', 'Tony', 'Debbie']

for p in range(n):
    l = input().strip()
    if l in full_name:
        idx = full_name.index(l)
        print(nick_name[idx])
    elif l in nick_name:
        idx = nick_name.index(l)
        print(full_name[idx])
    else:
        print('Not found')
