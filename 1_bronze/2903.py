import sys

input = sys.stdin.readline

n = int(input())

first_row_point_count = 2

point_count = 0

for _ in range(n):
    first_row_point_count = first_row_point_count * 2 - 1

    point_count = first_row_point_count ** 2

print(point_count)