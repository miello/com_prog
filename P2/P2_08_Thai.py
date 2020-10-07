list_text = {0: 'soon', 1: 'neung', 2: 'song', 3: 'sam', 4: 'si', 5: 'ha', 6: 'hok',
             7: 'chet', 8: 'paet', 9: 'kao', 10: 'sip', 20: 'yi sip', 100: 'roi', 1000: 'pun'}


def to_Thai(N):
    if 0 <= N <= 10:
        return list_text[N]
    text = []
    mul = 1
    while N != 0:
        now = (N % 10) * mul
        if now == 0:
            N //= 10
            mul *= 10
            continue
        if now == 1:
            text.append('et')
        elif list_text.get(now) and mul <= 10:
            text.append(list_text[now])
        else:
            text.append(list_text[mul])
            text.append(list_text[N % 10])
        mul *= 10
        N //= 10

    text = text[::-1]
    return ' '.join(text)


exec(input().strip())
