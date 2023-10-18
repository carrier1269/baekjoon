# import sys;from itertools import permutations, combinations

# K, M = map(int,sys.stdin.readline().split())

# def generate_primes(n):
#     primes = [False, False] + [True] * (n-1)
#     for i in range(2, int(n**0.5) + 1):
#         if primes[i]:
#             for j in range(i*2, n+1, i):
#                 primes[j] = False
#     return {x for x in range(2,n+1) if primes[x]}

# PRIME_LIST = generate_primes(10**K)

# count = 0

# def div(n, k):
#     if n < k: return n
#     while n % M == 0:
#         n //= M
#     return n

# def problem_1(n):
#     for i in range(2, n // 2 + 1):
#         if i != n-i and i in PRIME_LIST and n-i in PRIME_LIST:
#             return True
#     return False

# def problem_2(n):
#     while n % M == 0:
#         n //= M
#     for i in range(2, int(n ** 0.5) + 1):
#         if i in PRIME_LIST and n/i in PRIME_LIST:
#             return True
#     return False

# for i in permutations([x for x in range(10)], K):
#     if i[0] == 0:
#         continue

#     NUMBER = int(''.join(map(str, i)))

#     if problem_1(NUMBER):
#         if problem_2(NUMBER):
#             count += 1

# print(count)


import sys; input = sys.stdin.readline
from itertools import permutations

K, M = map(int,sys.stdin.readline().split())

is_prime = [True] * (10**K)

iter_range = int((10**K)**0.5)
for i in range(2, iter_range + 1):
    if is_prime[i]:
        for j in range(i+i, 10**K, i):
            is_prime[j] = False

count = 0

for i in permutations([x for x in range(10)], K):
    if i[0] == 0:
        continue

    NUMBER = int(''.join(map(str, i)))

    i = 2

    NUM = NUMBER
    while NUM % M == 0:
        NUM //= M

    for i in range(2, int(NUM ** 0.5) + 1):
        if NUM % i == 0:
            if is_prime[i] and is_prime[NUM//i]:
                for j in range(2, NUMBER // 2):
                    if is_prime[j] and is_prime[NUMBER-j]:
                        count += 1
                        break


print(count)

