month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

d, m, y = [int(e) for e in input().split('/')]

print('{} {}, {}'.format(month[m - 1], d, y))
