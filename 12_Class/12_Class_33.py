class piggybank:
    def __init__(self):
        self.cnt = [0, 0, 0, 0]
        self.value = [1, 2, 5, 10]

    def add1(self, n):
        self.cnt[0] += n

    def add2(self, n):
        self.cnt[1] += n

    def add5(self, n):
        self.cnt[2] += n

    def add10(self, n):
        self.cnt[3] += n

    def __int__(self):
        total = 0

        for i in range(4):
            total += self.cnt[i] * self.value[i]

        return total

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        temp = ', '.join(['{}:{}'.format(self.value[e], self.cnt[e]) for e in range(4)])

        return '{' + temp + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
