n = int(input())
map_text = dict()

for e in range(n):
    p = [int(x) for x in input().split()]
    temp = set(p)
    for q in temp:
        if not map_text.get(q):
            map_text[q] = 0
        map_text[q] += 1

union = 0
intersect = 0

for value in map_text.values():
    if value == n:
        intersect += 1
    if value >= 1:
        union += 1

print(union)
print(intersect)
