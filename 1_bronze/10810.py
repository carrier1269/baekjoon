import sys

input = sys.stdin.readline

n, m = map(int, input().split())

# bucket_list = list(map(int, "0" * n))
bucket_list = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())

    # bucket_list[i - 1 : j] = map(int, str(k) * (j - i + 1))

    for idx in range(i - 1, j):
        bucket_list[idx] = k

bucket_str = " ".join(map(str, bucket_list))

print(bucket_str)   