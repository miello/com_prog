def row_number(t, e):
    for i in range(len(t)):
        if e in t[i]:
            return i


def flatten(t):
    final = []
    for a in t:
        for b in a:
            if b != 0:
                final.append(b)
    return final


def inversions(x):
    cnt = 0
    for p in range(len(x)):
        for q in range(p + 1, len(x)):
            if x[p] > x[q]:
                cnt += 1
    return cnt


def solvable(t):
    arr = flatten(t)
    cnt_inversion = inversions(arr)
    if len(t) % 2 == 1:
        if cnt_inversion % 2 == 0:
            return True
        else:
            return False
    elif cnt_inversion % 2 == 1:
        idx_zero = row_number(t, 0)
        if idx_zero % 2 == 0:
            return True
        else:
            return False
    else:
        idx_zero = row_number(t, 0)
        if idx_zero % 2 == 1:
            return True
        else:
            return False


exec(input().strip())
