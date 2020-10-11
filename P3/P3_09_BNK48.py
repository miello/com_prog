query = 0

vote_list = dict()
score = dict()

kami_ochi = dict()
cnt_kami = dict()

while True:
    data = input().split()

    if len(data) == 1:
        query = int(data[0])
        break

    person = data[0]
    vote_to = data[1]
    vote_score = int(data[2])

    if not vote_list.get(person):
        vote_list[person] = dict()

    if not vote_list[person].get(vote_to):
        vote_list[person][vote_to] = 0
        kami_ochi[person] = ['', 0]

    cnt_kami[vote_to] = 0
    vote_list[person][vote_to] += vote_score

for x in list(vote_list.items()):
    person_name = x[0]
    for a in x[1]:
        name = a
        value = x[1][a]

        if not score.get(name):
            score[name] = [0, 0]

        score[name][0] += value
        score[name][1] += 1

        if kami_ochi[person_name][1] < value:
            kami_ochi[person_name][1] = value
            kami_ochi[person_name][0] = name
        elif kami_ochi[person_name][1] == value and kami_ochi[person_name][0] > name:
            kami_ochi[person_name][0] = name

for name, value in list(kami_ochi.values()):
    cnt_kami[name] += 1

if query == 1:
    ans = [e[0] for e in sorted(score.items(), key=lambda x: -x[1][0])][0:3]

elif query == 2:
    ans = [e[0] for e in sorted(score.items(), key=lambda x: -x[1][1])][0:3]

elif query == 3:
    ans = [e[0] for e in sorted(cnt_kami.items(), key=lambda x: -x[1])][0:3]

print(', '.join(ans))
