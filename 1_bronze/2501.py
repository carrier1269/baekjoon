import sys

input = sys.stdin.readline

n, k = map(int, input().split())

temp_list = []

for i in range(1, n + 1):
    if n % i == 0:
        temp_list.append(i)

try:
    print(temp_list[k - 1])
except:
    print(0)