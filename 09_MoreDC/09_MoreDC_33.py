def add_poly(p1, p2):
    memo = dict()

    for data in p1:
        memo[data[1]] = data[0]
    for data in p2:
        if not memo.get(data[1]):
            memo[data[1]] = 0
        memo[data[1]] += data[0]

    temp_list = []
    for expo, co in sorted(list(memo.items()), key=lambda x: -x[0]):
        if co != 0:
            temp_list.append((co, expo))

    return temp_list


def mult_poly(p1, p2):
    memo = dict()

    for co_1, expo_1 in p1:
        for co_2, expo_2 in p2:
            if not memo.get(expo_1 + expo_2):
                memo[expo_1 + expo_2] = 0
            memo[expo_1 + expo_2] += co_1 * co_2

    temp_list = []
    for expo, co in sorted(list(memo.items()), key=lambda x: -x[0]):
        if co != 0:
            temp_list.append((co, expo))

    return temp_list


for i in range(3):
    exec(input().strip())
