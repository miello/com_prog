class Complex:
    def __init__(self, a, b):
        self.real = a
        self.imagine = b

    def __str__(self):
        ans = ''
        if self.real != 0:
            ans += str(self.real)

        if self.imagine != 0:
            if self.imagine == -1:
                ans += '-i'
            else:
                if ans == '':
                    if self.imagine == 1:
                        ans += 'i'
                    else:
                        ans += str(self.imagine) + 'i'
                elif self.imagine == 1:
                    ans += '+i'
                elif self.imagine < 0:
                    ans += str(self.imagine) + 'i'
                else:
                    ans += '+' + str(self.imagine) + 'i'

        if ans == '':
            ans = '0'
        return ans

    def __add__(self, rhs):
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine

        result_real = a + c
        result_imagine = b + d

        return Complex(result_real, result_imagine)

    def __mul__(self, rhs):
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine

        result_real = a * c - b * d
        result_imagine = a * d + b * c

        return Complex(result_real, result_imagine)

    def __truediv__(self, rhs):
        a = self.real
        b = self.imagine
        c = rhs.real
        d = rhs.imagine

        result_real = (a * c + b * d) / (c ** 2 + d ** 2)
        result_imagine = (-a * d + b * c) / (c ** 2 + d ** 2)

        return Complex(result_real, result_imagine)
        pass


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1+c2)
elif t == 4:
    print(c1*c2)
else:
    print(c1/c2)
