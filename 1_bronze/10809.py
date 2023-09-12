import sys

input = sys.stdin.readline

a = str(input().rstrip())

alpha = "abcdefghijklmnopqrstuvwxyz" 

num_list = []

for i in alpha:
    if i in a:
        num_list.append(a.index(i))
    else:
        num_list.append(-1)

print(" ".join(map(str, num_list)))