import sys;input=sys.stdin.readline
n=int(input());arr = [0] * 2000001
for _ in range(n):
    a = int(input())
    if a >= 0:
        arr[a] += 1
    else:
        arr[-a+1000000] -= 1
for i in range(len(arr)-1, 1000000, -1):
    if arr[i] == -1:
        print(-(i - 1000000))
for j in range(len(arr)-1000000):
    if arr[j] == 1:
        print(j)