n = int(input())
win_dict = dict()

for i in range(n):
    win, lose = input().split()
    win_dict[lose] = False
    if win not in win_dict.keys():
        win_dict[win] = True
    else:
        win_dict[win] = True and win_dict[win]

print(sorted([key for key, value in win_dict.items() if value]))
