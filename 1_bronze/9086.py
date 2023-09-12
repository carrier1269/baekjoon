import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = str(input().rstrip())

    print(f'{string[0]}{string[-1]}')