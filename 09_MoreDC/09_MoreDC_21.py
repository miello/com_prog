def factor(N):
    prime = []
    for p in range(2, int(N ** (0.5))):
        if N % p == 0:
            cnt = 0
            while N % p == 0:
                cnt += 1
                N //= p
            prime.append([p, cnt])
    if N != 1:
        prime.append([N, 1])
    return prime


exec(input().strip())
