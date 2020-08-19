def distance1(x1, y1, x2, y2):
    dx = (x2 - x1) ** 2
    dy = (y2 - y1) ** 2
    return (dx + dy) ** (0.5)


def distance2(p1, p2):
    return distance1(p1[0], p1[1], p2[0], p2[1])


def distance3(c1, c2):
    dist = distance2(c1[0:2], c2[0:2])
    return dist, (c1[2] + c2[2]) >= dist


def perimeter(points):
    l = 0
    for p in range(len(points) - 1):
        l += distance2(points[p], points[p + 1])
    l += distance2(points[0], points[len(points) - 1])
    return l


exec(input().strip())
