import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst1 = []
lst2 = []

for i in range(n):
    temp_lst = list(map(int, input().split()))
    lst1.append(temp_lst)

for j in range(n):
    temp_lst = list(map(int, input().split()))
    lst2.append(temp_lst)

for a in range(n):
    for b in range(m):
        lst1[a][b] += lst2[a][b]

for x in range(n):
    print(" ".join(map(str, lst1[x][:])))