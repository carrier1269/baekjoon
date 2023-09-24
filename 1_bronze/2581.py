import sys

input = sys.stdin.readline

m = int(input())

n = int(input())

number_list = []

for i in range(m, n + 1):
    temp_list = []

    for j in range(2, i + 1):
        if i % j == 0:
            temp_list.append(j)
    if len(temp_list) == 1:
        number_list.append(i)

if len(number_list) != 0:
    print("{}\n{}".format(sum(number_list), min(number_list)))
else:
    print(-1)