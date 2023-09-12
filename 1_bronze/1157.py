import sys

input = sys.stdin.readline

string = str(input().rstrip())

string = string.lower()

alpha_list = []

for a in string:
    alpha_list.append(a)

alpha_set = set(alpha_list)

temp = list(alpha_set)

num_count_list = []

for i in alpha_set:
    num_count_list.append(alpha_list.count(i))

max_count = max(num_count_list)

dup_count = 0 
fin_count = 0

for j in num_count_list:
    if max_count == j:
        dup_count += 1

    if dup_count >= 2:
        print("?")
        break

    fin_count += 1

    if fin_count == len(num_count_list):
        print(temp[num_count_list.index(max_count)].upper())