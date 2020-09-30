n = int(input())

price = dict()

for i in range(n):
    name, price_i = input().split()
    price[name] = float(price_i)

total_price = 0
popular_name = []
popular_price = 0

m = int(input())
quantity_cnt = dict()

for i in range(m):
    name, quantity = input().split()
    if not quantity_cnt.get(name):
        quantity_cnt[name] = 0.0
    quantity_cnt[name] += float(quantity)

for key, val in quantity_cnt.items():
    if price.get(key):
        price_cal = price[key] * val
        total_price += price_cal
        if price_cal > popular_price:
            popular_name = [key]
            popular_price = price_cal
        elif price_cal == popular_price:
            popular_name.append(key)


if len(popular_name) == 0:
    print('No ice cream sales')
else:
    popular_name.sort()
    print('Total ice cream sales: {}'.format(total_price))
    print('Top sales: {}'.format(', '.join(popular_name)))
