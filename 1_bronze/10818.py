import sys

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

max = max(num_list)
min = min(num_list)

print(f'{min} {max}')