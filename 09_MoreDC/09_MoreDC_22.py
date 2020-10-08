def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m


def mult_c(c, A):
    x = len(A)
    y = len(A[0])
    temp = [[0 for e in range(y)] for e in range(x)]
    for p in range(0, x):
        for q in range(0, y):
            temp[p][q] = A[p][q] * c
    return temp


def mult(A, B):
    x = len(A)
    t = len(A[0])
    y = len(B[0])
    temp = [[0 for e in range(y)] for e in range(x)]
    for p in range(0, x):
        for q in range(0, y):
            for r in range(0, t):
                temp[p][q] += A[p][r] * B[r][q]
    return temp


exec(input().strip())
