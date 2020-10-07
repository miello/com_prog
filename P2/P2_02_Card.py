card_pack = {'C': 1, 'D': 2, 'H': 3, 'S': 4}
card_value = {'A': 1, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}

for i in range(2, 10):
    card_value[str(i)] = i

card_set = input()

for i in range(0, len(card_set) - 2, 2):
    value_1 = card_value[card_set[i]]
    value_2 = card_value[card_set[i + 2]]
    value_net = 0
    if value_1 != value_2:
        value_net = value_1 - value_2
    else:
        value_net = card_pack[card_set[i + 1]] - card_pack[card_set[i + 3]]
    if value_net > 0:
        value_net = '+' + str(value_net)
    print(value_net, end='')
