month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mname = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]


def zodiac(d1, m1):
    z1 = None
    if d1 >= 22 and m1 == 3 or d1 <= 21 and m1 == 4:
        z1 = "Aries"
    elif d1 >= 22 and m1 == 4 or d1 <= 21 and m1 == 5:
        z1 = "Taurus"
    elif d1 >= 22 and m1 == 5 or d1 <= 21 and m1 == 6:
        z1 = "Gemini"
    elif d1 >= 22 and m1 == 6 or d1 <= 21 and m1 == 7:
        z1 = "Cancer"
    elif d1 >= 22 and m1 == 7 or d1 <= 21 and m1 == 8:
        z1 = "Leo"
    elif d1 >= 22 and m1 == 8 or d1 <= 21 and m1 == 9:
        z1 = "Virgo"
    elif d1 >= 22 and m1 == 9 or d1 <= 21 and m1 == 10:
        z1 = "Libra"
    elif d1 >= 22 and m1 == 10 or d1 <= 21 and m1 == 11:
        z1 = "Scorpio"
    elif d1 >= 22 and m1 == 11 or d1 <= 21 and m1 == 12:
        z1 = "Sagittarius"
    elif d1 >= 22 and m1 == 12 or d1 <= 20 and m1 == 1:
        z1 = "Capricorn"
    elif d1 >= 21 and m1 == 1 or d1 <= 20 and m1 == 2:
        z1 = "Aquarius"
    elif d1 >= 21 and m1 == 2 or d1 <= 21 and m1 == 3:
        z1 = "Pisces"
    return z1


def days_in_feb(y1):
    if y1 % 400 == 0 or y1 % 100 != 0 and y1 % 4 == 0:
        return 29
    return 28


def days_in_month(m, y):
    if m == 2:
        return days_in_feb(y)
    else:
        return month[m - 1]


def days_in_between(d1, m1, y1, d2, m2, y2):
    diff = 0
    for idx in range(m1 + 1, 13):
        diff += days_in_month(idx, y1)
    for idx in range(1, m2):
        diff += days_in_month(idx, y2)
    diff += int((y2 - y1 - 1)*365.25)
    diff += d2 - 1
    diff += days_in_month(m1, y1) - d1 + 1
    return diff


def read_date():
    p = input().split()
    p[0] = int(p[0])
    p[1] = mname.index(p[1][:3]) + 1
    p[2] = int(p[2])
    return p


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()

    z1 = zodiac(d1, m1)
    z2 = zodiac(d2, m2)

    days = days_in_between(d1, m1, y1, d2, m2, y2)

    print(z1, z2)
    print(days)


exec(input().strip())
