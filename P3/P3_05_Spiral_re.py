def spiral_square(n):
    ans = [[0 for e in range(n)] for e in range(n)]

    now = 1
    idx_di = 0
    di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    x = n // 2
    y = n // 2
    cnt = 0

    ans[x][y] = now

    while now < n ** 2:

        temp = cnt

        if idx_di == 0 or idx_di == 2:
            cnt += 1

        while x >= 0 and y >= 0 and x <= n - 1 and y <= n - 1 and temp >= 0:
            ans[x][y] = now
            x += di[idx_di][0]
            y += di[idx_di][1]
            temp -= 1
            now += 1

        x -= di[idx_di][0]
        y -= di[idx_di][1]

        idx_di = (idx_di + 1) % 4

        now -= 1

    return ans


def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2 * ' ' + str(e))[-3:] for e in S[i]]))


exec(input().strip())
