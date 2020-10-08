def pattern1(nrows, ncols):
    final_list = [[0 for e in range(ncols)] for e in range(nrows)]
    now = 1
    for i in range(0, nrows):
        for j in range(0, ncols):
            final_list[i][j] = now
            now += 1
    return final_list


def pattern2(nrows, ncols):
    final_list = [[0 for e in range(ncols)] for e in range(nrows)]
    now = 1

    for i in range(0, ncols):
        for j in range(0, nrows):
            final_list[j][i] = now
            now += 1

    return final_list


def pattern3(N):
    final_list = [[0 for e in range(N)] for e in range(N)]
    now = 1

    for i in range(0, N):
        for j in range(i, N):
            final_list[i][j] = now
            now += 1

    return final_list


def pattern4(N):
    final_list = [[0 for e in range(N)] for e in range(N)]
    now = 1

    for i in range(0, N):
        for j in range(i, -1, -1):
            final_list[j][i] = now
            now += 1

    return final_list


def pattern5(N):
    final_list = [[0 for e in range(N)] for e in range(N)]
    now = 1

    for i in range(0, N):
        for j in range(0, N - i):
            final_list[j][i + j] = now
            now += 1

    return final_list


def pattern6(N):
    final_list = [[0 for e in range(N)] for e in range(N)]
    now = 1

    for i in range(0, N, 2):
        for j in range(0, N - i):
            final_list[j][i + j] = now
            now += 1
        for j in range(N - i - 2, -1, -1):
            final_list[j][i + 1 + j] = now
            now += 1

    return final_list


exec(input().strip())
