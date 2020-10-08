def knows(R, x, y):
    return y in R[x]


def is_celeb(R, x):
    for q in R.keys():
        if x not in R[q] and q != x:
            return False
    return True


def find_celeb(R):
    for p in R.keys():
        if is_celeb(R, p):
            return p


def read_relations():
    R = dict()

    while True:
        d = input().split()
        if len(d) == 1:
            break

        if not R.get(d[0]):
            R[d[0]] = set()
        if not R.get(d[1]):
            R[d[1]] = set()

        R[d[0]].add(d[1])

    return R


def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print('Not Found')
    else:
        print(c)


exec(input().strip())  # do not remove this line
