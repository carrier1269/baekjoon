import sys

input = sys.stdin.readline

num = int(input())

for i in range(2 * num):
    if i == 0:
        continue
    elif i <= num:
        print(" " * (num - i) + "*" * (2 * i - 1))
    else:
        j = (num * 2) - i
        i -= num
        print(" " * i + "*" * (2 * j - 1))