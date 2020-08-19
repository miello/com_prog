while True:
    text = input().strip()

    if text == 'end':
        break
    text = list(text)

    for idx in range(len(text)):
        data = text[idx]
        if 'A' <= data <= 'Z':
            num = ((ord(data) - 65) + 13) % 26
            text[idx] = chr(num + 65)
        elif 'a' <= data <= 'z':
            num = ((ord(data) - 97) + 13) % 26
            text[idx] = chr(num + 97)
        else:
            text[idx] = data

    print("".join(text))
