import sys

input = sys.stdin.readline

lst = []

for _ in range(9):
    temp_lst = list(map(int, input().split()))

    lst.append(temp_lst)

max = 0
last_i, last_j = 0, 0

for i in range(9):
    for j in range(9):
        if lst[i][j] > max:
            max = lst[i][j]

            last_i, last_j = i, j
print(max)
print("{} {}".format(last_i + 1, last_j + 1))        