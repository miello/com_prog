def spiral_square(n):
    ans = [[0 for e in range(n)] for e in range(n)]

    now = n ** 2
    idx_di = 0
    di = [[0, -1], [-1, 0], [0, 1], [1, 0]]

    x = n - 1
    y = n - 1

    while now >= 1:
        while x >= 0 and y >= 0 and x <= n - 1 and y <= n - 1:
            if ans[x][y] != 0:
                break
            ans[x][y] = now
            x += di[idx_di][0]
            y += di[idx_di][1]
            now -= 1

        x -= di[idx_di][0]
        y -= di[idx_di][1]

        idx_di = (idx_di + 1) % 4

        x += di[idx_di][0]
        y += di[idx_di][1]

    return ans


def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2 * ' ' + str(e))[-3:] for e in S[i]]))


exec(input().strip())
