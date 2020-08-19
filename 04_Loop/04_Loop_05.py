tar = input().strip()
line = input().strip()
sep = ['\"', '(', '\'', ')', ',', '.', ' ']
co = 0
word = []
temp = ""

for l in line:
    if l in sep:
        print(l)
        word.append(temp)
        temp = ""
    else:
        temp += l

word.append(temp)

print(word.count(tar))
