def first_fit(L, e):
    found = False

    for p in L:
        if sum(p) + e <= 100:
            p.append(e)
            found = True
            break

    if not found:
        L.append([e])
    return L


def best_fit(L, e):
    mx = -1

    for p in L:
        if sum(p) + e <= 100:
            mx = max(sum(p) + e, mx)

    for p in L:
        if mx == sum(p) + e:
            p.append(e)

    if mx == -1:
        L.append([e])

    return L


def partition_FF(D):
    final_list = []

    for p in D:
        first_fit(final_list, p)

    return final_list


def partition_BF(D):
    final_list = []

    for p in D:
        best_fit(final_list, p)

    return final_list


exec(input().strip())
