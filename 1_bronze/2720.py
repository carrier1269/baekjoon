import sys

input = sys.stdin.readline

coin = [0.25 * 100, 0.10 * 100, 0.05 * 100, 0.01 * 100]

t = int(input())

coin_count = []

for _ in range(t):
    a = int(input())

    for i in coin:
        if a / i > 0:
            coin_temp_count = a // i

            a %= i

            coin_count.append(int(coin_temp_count))
        else:
            coin_count.append(0)

    print(" ".join(map(str, coin_count)))

    coin_count.clear()