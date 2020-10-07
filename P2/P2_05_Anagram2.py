dict_1 = dict()
dict_2 = dict()

text_1 = input()
text_2 = input()
remove_a = []
remove_b = []

for ch in text_1:
    ch = ch.lower()
    if not 'a' <= ch <= 'z':
        continue
    if not dict_1.get(ch):
        dict_1[ch] = 0
    dict_1[ch] += 1

for ch in text_2:
    ch = ch.lower()
    if not 'a' <= ch <= 'z':
        continue
    if not dict_2.get(ch):
        dict_2[ch] = 0
    dict_2[ch] += 1

for ch in list(dict_1.keys()):
    val_1 = dict_1[ch]
    val_2 = 0
    if dict_2.get(ch):
        val_2 = dict_2[ch]
    if val_1 > val_2:
        remove_a.append((val_1 - val_2, ch))

for ch in list(dict_2.keys()):
    val_1 = 0
    if dict_1.get(ch):
        val_1 = dict_1[ch]
    val_2 = dict_2[ch]
    if val_2 > val_1:
        remove_b.append((val_2 - val_1, ch))

print(text_1)
if len(remove_a) == 0:
    print(' - None')
else:
    remove_a.sort(key=lambda x: x[1])
    for ch in remove_a:
        print(' - remove {} {}'.format(ch[0], ch[1]), end='')
        if ch[0] > 1:
            print('\'s')
        else:
            print()

print(text_2)
if len(remove_b) == 0:
    print(' - None')
else:
    remove_b.sort(key=lambda x: x[1])
    for ch in remove_b:
        print(' - remove {} {}'.format(ch[0], ch[1]), end='')
        if ch[0] > 1:
            print('\'s')
        else:
            print()
