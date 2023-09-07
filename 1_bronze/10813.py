import sys

input = sys.stdin.readline

n, m = map(int, input().split())

bucket_list = []

for i in range(1, n + 1):
    bucket_list.append(i)

for _ in range(m):
    i, j = map(int, input().split())

    bucket_list[i - 1], bucket_list[j - 1] = bucket_list[j - 1], bucket_list[i - 1]

print(" ".join(map(str, bucket_list)))