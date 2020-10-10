class piggybank:
    def __init__(self):
        self.coins = dict()

    def add(self, v, n):
        v = float(v)
        if sum(self.coins.values()) + n > 100:
            return False

        if not self.coins.get(v):
            self.coins[v] = 0

        self.coins[v] += n

        return True

    def __float__(self):
        total = 0.0

        for key, value in self.coins.items():
            total += key * value

        return total

    def __str__(self):
        ans = []

        for key, value in sorted(self.coins.items(), key=lambda x: x[0]):
            ans.append('{}:{}'.format(key, value))

        return '{' + ', '.join(ans) + '}'


cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank()
p2 = piggybank()
for c in cmd1:
    eval(c)
for c in cmd2:
    eval(c)
