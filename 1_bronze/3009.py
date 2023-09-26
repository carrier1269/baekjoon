import sys

input = sys.stdin.readline

temp_x_list = []
temp_y_list = []

for _ in range(3):
    a, b = map(int, input().split())

    temp_x_list.append(a);temp_y_list.append(b)

print("{} {}".format(max(temp_x_list) if temp_x_list.count(min(temp_x_list))==2 else min(temp_x_list), 
                     max(temp_y_list) if temp_y_list.count(min(temp_y_list))==2 else min(temp_y_list)))