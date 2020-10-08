def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(a, b, c):
    return gcd(a, gcd(b, c)) == 1


def primitive_Pythagorean_triples(max_len):
    triple = []
    max_len += 1
    for i in range(1, max_len):
        for j in range(i, max_len):
            for k in range(j, max_len):
                if (i ** 2) + (j ** 2) == k ** 2 and is_coprime(i, j, k):
                    triple.append([i, j, k])
    triple.sort(key=lambda x: (x[2], x[0]))
    return triple


exec(input().strip())
