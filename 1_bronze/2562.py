import sys

input = sys.stdin.readline

num_list = []

for _ in range(9):
    num_list.append(int(input()))

max = max(num_list)

where = num_list.index(max)

print(f'{max}\n{where + 1}')