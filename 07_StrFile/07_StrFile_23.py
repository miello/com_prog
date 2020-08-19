text, year = input().split()
mx = -1
mn = 101.0
co = 0
sum_score = 0
year = int(year) % 100

with open(text, 'r') as q:
    while True:
        line = q.readline()
        if not line:
            break
        line = line.split()
        id = line[0]
        score = float(line[1])
        if id[0:2] == str(year):
            mx = max(score, mx)
            mn = min(score, mn)
            sum_score += score
            co += 1

if co == 0:
    print('No data')
    exit()

print(mn, mx, sum_score / co)
