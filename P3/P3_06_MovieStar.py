n = int(input())

actor = dict()

for p in range(n):
    movie_name, actor_1, actor_2 = input().split(',')
    movie_name = movie_name.strip()
    actor_1 = actor_1.strip()
    actor_2 = actor_2.strip()
    if not actor.get(actor_1):
        actor[actor_1] = []
    if not actor.get(actor_2):
        actor[actor_2] = []
    actor[actor_1].append(movie_name)
    actor[actor_2].append(movie_name)

query = input().split(',')
for data in query:
    data = data.strip()
    print('{} -> '.format(data), end='')
    if not actor.get(data):
        print('Not found')
    else:
        print(', '.join(actor[data]))
