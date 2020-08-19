sol = input().strip('\n')
ans = input().strip('\n')

if len(ans) != len(sol):
    print('Incomplete answer')
else:
    score = 0
    for i in range(len(ans)):
        if sol[i] == ans[i]:
            score += 1
    print(score)
