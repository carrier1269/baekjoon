import sys

input = sys.stdin.readline

n, m = map(int, input().split())

bucket_list = []

for i in range(1, n + 1):
    bucket_list.append(i)

bucket_list.sort()

new_bucket_list = []

for _ in range(m):
    i, j = map(int, input().split())

    for a in bucket_list[j - n -1 : i - n -2 : -1]:
        new_bucket_list.append(a)

    bucket_list[i - 1 : j] = new_bucket_list

    new_bucket_list = []

print(" ".join(map(str, bucket_list)))
