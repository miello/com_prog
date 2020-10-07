def is_odd(n):
    return n % 2 == 1


def has_odds(x):
    for l in x:
        if is_odd(l):
            return True
    return False


def all_odds(x):
    return len([e for e in x if e % 2 == 1]) == len(x)


def no_odds(x):
    return len([e for e in x if e % 2 == 0]) == len(x)


def get_odds(x):
    return [e for e in x if e % 2 == 1]


def zip_odds(a, b):
    odd_a = get_odds(a)
    odd_b = get_odds(b)
    new_arr = []

    switch = 0
    now_a = 0
    len_a = len(odd_a)
    now_b = 0
    len_b = len(odd_b)

    while now_a < len_a and now_b < len_b:
        if switch == 0:
            new_arr.append(odd_a[now_a])
            now_a += 1
        else:
            new_arr.append(odd_b[now_b])
            now_b += 1
        switch ^= 1

    while now_a < len_a:
        new_arr.append(odd_a[now_a])
        now_a += 1

    while now_b < len_b:
        new_arr.append(odd_b[now_b])
        now_b += 1

    return new_arr


exec(input().strip())
