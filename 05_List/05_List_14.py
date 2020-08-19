inp = [int(e) for e in input().split()]
co = 0

for p in range(1, len(inp) - 1):
    if inp[p - 1] < inp[p] and inp[p] > inp[p + 1]:
        co += 1

print(co)
