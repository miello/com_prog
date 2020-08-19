import math

n = input().split(',')

num_ans_1 = int(n[0])
de_ans_1 = 1

mid_mo = int('0' + n[1])
num_ans_2 = mid_mo
de_ans_2 = 10 ** (len(n[1]))

len_last = len(n[2])
num_ans_3 = int(n[2])
de_ans_3 = de_ans_2 * (10 ** (len_last) - 1)

de_frac = de_ans_3
num_frac = (num_ans_1 * de_ans_3) + (num_ans_2 * (de_frac // de_ans_2)) + num_ans_3

gcd = math.gcd(num_frac, de_frac)
num_frac //= gcd
de_frac //= gcd

print('{} / {}'.format(num_frac, de_frac))
