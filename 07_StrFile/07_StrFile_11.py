p = list(input().strip())
vowel = ['a', 'e', 'i', 'o', 'u']

if p[-1] == 'x' or p[-1] == 's' or p[-1] == 'h' and p[-2] == 'c':
    p += list('es')
elif p[-1] == 'y' and p[-2] not in vowel:
    p[-1] = 'i'
    p += list('es')
else:
    p += list('s')

print("".join(p))
