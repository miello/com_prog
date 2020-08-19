def make_int_list(x):
    return [int(e) for e in x.split()]


def is_odd(e):
    return bool(e & 1)


def odd_list(alist):
    return [data for data in alist if data & 1]


def sum_square(alist):
    ans = 0
    for data in alist:
        ans += data ** 2
    return ans


exec(input().strip())
