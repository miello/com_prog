score_list = {'X': 0, 'R': 1, 'Y': 2, 'G': 3, 'W': 4, 'B': 5, 'P': 6, 'K': 7}

score = [0, 0]
p = 0

while p < 12:
    temp = input().strip()
    player = ord(temp[0]) - ord('1')
    play_list = temp[1:]
    if play_list[0] == 'X':
        p -= 1
    for l in play_list:
        score[player] += score_list[l]
    p += 1

print(score[0], score[1])

if score[0] < score[1]:
    print('Player 2 wins')
elif score[0] > score[1]:
    print('Player 1 wins')
else:
    print('Tie')
