def convert(text):
    if text == 'J':
        return 11
    if text == 'Q':
        return 12
    if text == 'K':
        return 13
    if text == 'A':
        return 14
    if text == '2':
        return 15
    return int(text)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + self.value + ' ' + self.suit + ')'

    def getScore(self):
        if self.value == 'A':
            return 1
        elif 'A' <= self.value <= 'Z':
            return 10
        return int(self.value)

    def sum(self, other):
        return (self.getScore() + other.getScore()) % 10

    def __lt__(self, rhs):
        val_self = convert(self.value)
        val_rhs = convert(rhs.value)
        if val_self != val_rhs:
            return val_self < val_rhs
        else:
            return mp[self.suit] < mp[rhs.suit]


mp = {'club': 1, 'diamond': 2, 'heart': 3, 'spade': 4}
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])
