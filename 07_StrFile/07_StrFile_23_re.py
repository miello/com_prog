text, year = input().split()

data_file = open(text, 'r')

data = data_file.read().splitlines()

year_filter = [float(e.split()[1]) for e in data if e.split()[0][:2] == year[-2:]]

if len(year_filter) == 0:
    print('No data')
    exit()

print(min(year_filter), max(year_filter), sum(year_filter) / len(year_filter))
