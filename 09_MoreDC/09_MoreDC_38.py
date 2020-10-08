station_data = dict()

while True:
    p = input().split()

    if len(p) == 1:
        final = dict()
        query = p[0]

        if not station_data.get(query):
            print(query)
            break

        for q in station_data[query]:
            final[q] = True
            for r in station_data[q]:
                final[r] = True

        temp_list = list(final.keys())

        for l in sorted(temp_list):
            print(l)

        break

    if not station_data.get(p[0]):
        station_data[p[0]] = []
    if not station_data.get(p[1]):
        station_data[p[1]] = []

    station_data[p[0]].append(p[1])
    station_data[p[1]].append(p[0])
