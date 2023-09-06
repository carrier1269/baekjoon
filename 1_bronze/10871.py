import sys

input = sys.stdin.readline

n, x = map(int, input().split())

num_list = list(map(int, input().split()))

result_list = []

for i in range(n):
    if num_list[i] < x:
        result_list.append(num_list[i])

result_str = ""
for j in range(len(result_list)):
    result_str += (str(result_list[j]) + " ")

print(result_str)