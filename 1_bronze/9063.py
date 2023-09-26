import sys

input = sys.stdin.readline

n = int(input())

temp_x_list = []
temp_y_list = []

for _ in range(n):
    a, b = map(int, input().split())

    temp_x_list.append(a), temp_y_list.append(b)

under_length = max(temp_x_list) - min(temp_x_list)
side_length = max(temp_y_list) - min(temp_y_list)

print(under_length * side_length)