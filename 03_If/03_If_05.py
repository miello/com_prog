p = int(input())

ans_1 = ''
ans_2 = ''

if p > 0:
    ans_1 = 'positive'
elif p < 0:
    ans_1 = 'negative'
else:
    ans_1 = 'zero'

if p & 1:
    ans_2 = 'odd'
else:
    ans_2 = 'even'

print(ans_1)
print(ans_2)
