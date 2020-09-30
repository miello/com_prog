name_to_nick = dict()
nick_to_name = dict()

n = int(input())

for i in range(n):
    name, nick = input().split()
    name_to_nick[name] = nick
    nick_to_name[nick] = name

m = int(input())

for i in range(m):
    name = input()
    if name_to_nick.get(name):
        print(name_to_nick[name])
    elif nick_to_name.get(name):
        print(nick_to_name[name])
    else:
        print('Not found')
