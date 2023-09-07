import sys

input = sys.stdin.readline

num_true_list = []

for _ in range(28):
    num_true_list.append(int(input()))

num_true_list.sort()

num_null_list = []

for i in range(1, 31):
    if i not in num_true_list:
        num_null_list.append(i)

print(f'{num_null_list[0]}\n{num_null_list[1]}')