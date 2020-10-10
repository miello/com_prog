class roman:
    def __init__(self, r):
        self.data = r

        self.roman = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        self.numeric = dict()

        for key, value in self.roman.items():
            self.numeric[value] = key

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        return self.data

    def __int__(self):

        idx = 0
        result = 0
        l = self.data

        while idx < len(l):
            if self.numeric.get(l[idx:idx + 2]):
                result += self.numeric[l[idx:idx + 2]]
                idx += 2
            else:
                result += self.numeric[l[idx]]
                idx += 1

        return result

    def __add__(self, rhs):
        p = int(self)
        q = int(rhs)

        temp = p + q
        p = []

        while temp != 0:
            p.append(temp % 10)
            temp //= 10

        mul = 10 ** (len(p) - 1)
        p = p[::-1]
        ans = []
        for q in p:
            if q == 0:
                continue
            if mul == 10 ** 3:
                ans.append(self.roman[mul] * q)
            elif self.roman.get(q * mul):
                ans.append(self.roman[q * mul])
            elif q < 4:
                ans.append(self.roman[mul] * q)
            elif q > 5:
                ans.append(self.roman[5 * mul] + self.roman[mul] * (q - 5))
            mul //= 10
        return roman(''.join(ans))


t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)
if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
