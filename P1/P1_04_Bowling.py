frame_str = input().strip()
frame = []
score = [0] * 10
question = int(input())

idx_now = 0
cnt_frame = 0

while cnt_frame < 9:
    if frame_str[idx_now] == 'X':
        frame.append(frame_str[idx_now])
        idx_now += 1
    else:
        frame.append(frame_str[idx_now: idx_now + 2])
        idx_now += 2
    cnt_frame += 1

frame.append(frame_str[idx_now:])

for i in range(0, 9):
    if frame[i][0] == 'X':
        score[i] = 10
        if len(frame[i + 1]) == 1:
            score[i] += 10
            if frame[i + 2][0] == 'X':
                score[i] += 10
            else:
                score[i] += int(frame[i + 2][0])
        else:
            prev = 0
            for data in frame[i + 1][:2]:
                if data == 'X':
                    score[i] += 10
                elif data == '/':
                    score[i] += 10 - prev
                else:
                    score[i] += int(data)
                    prev = int(data)
    elif frame[i][1] == '/':
        score[i] = 10
        if frame[i + 1][0] == 'X':
            score[i] += 10
        else:
            score[i] += int(frame[i + 1][0])
    else:
        for data in frame[i]:
            score[i] += int(data)

if len(frame[9]) == 2:
    for data in frame[9]:
        score[i] += int(data)
else:
    prev = 0
    for data in frame[9]:
        if data == 'X':
            score[9] += 10
        elif data == '/':
            score[9] += 10 - prev
        else:
            score[9] += int(data)
            prev = int(data)

if 1 <= question <= 10:
    print(score[question - 1])
else:
    print(sum(score))
