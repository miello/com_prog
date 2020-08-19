n = int(input().strip())

win_a = 0
win_b = 0

for i in range(3 * n):
    p, q = input().strip().split()
    if p == q:
        continue
    elif p == 'R':
        if q == 'P':
            win_b += 1
        else:
            win_a += 1
    elif p == 'S':
        if q == 'R':
            win_b += 1
        else:
            win_a += 1
    else:
        if q == 'S':
            win_b += 1
        else:
            win_a += 1
    if win_a == n:
        print('{} {}'.format(win_a, win_b))
        print('Player 1 wins')
        exit()
    elif win_b == n:
        print('{} {}'.format(win_a, win_b))
        print('Player 2 wins')
        exit()

print('{} {}'.format(win_a, win_b))
print('Tie')
