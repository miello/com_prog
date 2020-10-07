def convex_polygon_area(p):
    p.append(p[0])
    det = 0
    for e in range(len(p) - 1):
        det += p[e][0] * p[e + 1][1]
        det -= p[e][1] * p[e + 1][0]
    return abs(det) / 2
    pass


def is_heterogram(s):
    dup = dict()
    for e in s:
        ch = e.lower()
        if not 'a' <= ch <= 'z':
            continue
        if ch not in dup:
            dup[ch] = True
        else:
            return False
    return True
    pass


def replace_ignorecase(s, a, b):
    len_a = len(a)
    a = ''.join([e.lower() for e in a])
    final_str = []
    e = 0
    while e < len(s):
        old_str = ''
        if e + len_a - 1 < len(s):
            old_str = ''.join([p.lower() for p in s[e:e + len_a]])
        if old_str != a:
            final_str.append(s[e])
            e += 1
        else:
            final_str.append(b)
            e += len_a
    return ''.join(final_str)


def top3(votes):
    values_list = list(votes.items())
    values_list.sort(key=lambda x: (-x[1], x[0]))
    ans = [values_list[e][0] for e in range(min(3, len(values_list)))]
    return ans


for k in range(2):
    exec(input().strip())
