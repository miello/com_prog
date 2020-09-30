def total(pocket):
    total_money = 0
    for key, val in pocket.items():
        total_money += key * val
    return total_money


def take(pocket, money_in):
    for key, val in money_in.items():
        if not pocket.get(key):
            pocket[key] = 0
        pocket[key] += val


def pay(pocket, amt):
    list_pay = dict()
    temp = list(pocket.items())
    temp.sort(reverse=True)

    for key, val in temp:
        coin_cnt = min(val, amt // key)
        if coin_cnt == 0:
            continue
        pocket[key] -= coin_cnt
        list_pay[key] = coin_cnt
        amt -= key * coin_cnt

    if amt > 0:
        for key, val in list_pay.items():
            pocket[key] += val
        return dict()

    return list_pay


exec(input().strip())
