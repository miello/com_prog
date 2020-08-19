data = list(input())

for idx, ch in enumerate(data):
    if ch == '(':
        data[idx] = '['
    elif ch == '[':
        data[idx] = '('
    elif ch == ')':
        data[idx] = ']'
    elif ch == ']':
        data[idx] = ')'

print("".join(data))
