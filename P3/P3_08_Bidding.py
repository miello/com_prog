n = int(input())

auction_log = dict()
auction_result = dict()

for i in range(n):
    data = input().split()

    person = data[1]
    asset = data[2]

    if data[0] == 'B':

        price = int(data[3])

        if not auction_log.get(asset):
            auction_log[asset] = []
        for p in auction_log.get(asset):
            if p[0] == person:
                p[2] = False
        auction_log[asset].append([person, price, True])

    else:
        if auction_log.get(asset):
            for value in auction_log[asset]:
                if value[0] == person:
                    value[2] = False

    auction_result[person] = [0, []]

temp = list(auction_log.items())

for x in temp:
    asset_name = x[0]
    winner_name = ''
    winner_price = 0

    for name, price, status in x[1]:
        if status:
            if winner_price < price:
                winner_price = price
                winner_name = name

    if winner_name != '':
        auction_result[winner_name][0] += winner_price
        auction_result[winner_name][1].append(asset_name)

for name, l in sorted(auction_result.items()):
    print('{}: ${}'.format(name, l[0]), end='')
    if l[0] != 0:
        print(' -> {}'.format(' '.join(sorted(l[1]))), end='')
    print()
