p = input().split()

final_list = []

t = None

for ch in p:
    t = ''
    for text in ch:
        if 'a' <= text <= 'z' or 'A' <= text <= 'Z' or '0' <= text <= '9':
            t += text
        else:
            if t != '':
                final_list.append(t)
            t = ''
    if t != '':
        final_list.append(t)

temp = final_list[0]
rep = ''

print(final_list)

for p in temp:
    if 'A' <= p <= 'Z':
        rep += chr(ord(p) + 32)
    else:
        rep += p

final_list[0] = rep

for p in range(1, len(final_list)):
    temp = final_list[p]
    if 'a' <= temp[0] <= 'z':
        final_list[p] = chr(ord(temp[0]) - 32)
    else:
        final_list[p] = temp[0]
    for q in range(1, len(temp)):
        if 'A' <= temp[q] <= 'Z':
            final_list[p] += chr(ord(temp[q]) + 32)
        else:
            final_list[p] += temp[q]

print("".join(final_list))
