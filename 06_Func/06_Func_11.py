def bin(x):
    p = []
    while x != 0:
        p.append(str(int(x) & 1))
        x //= 2
    p = p[::-1]
    if len(p) == 0:
        return '0'
    return "".join(p)


def base(x, bas=10):
    now = 1
    ans = 0
    x = x[::-1]
    for ch in x:
        ans += now * int(ch)
        now *= bas
    return ans


data = input().split()
x = base(data[0], 2)
y = base(data[1], 2)

print(bin(x + y))
