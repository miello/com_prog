pack_value = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2', '3']
pack_suit = ['club', 'diamond', 'heart', 'spade']


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str('({} {})'.format(self.value, self.suit))
        pass

    def next1(self):
        x = pack_value.index(self.value)
        y = pack_suit.index(self.suit)

        y += 1
        if y == 4:
            x += 1
            y = 0

        return Card(pack_value[x], pack_suit[y])

    def next2(self):
        temp = self.next1()
        self.value = temp.value
        self.suit = temp.suit


n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
