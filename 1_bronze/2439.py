import sys

input = sys.stdin.readline

num = int(input())

for i in range(1, num + 1):
    j = num - i

    print(f'{" " * j}{"*" * i}')