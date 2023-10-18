import sys;input=sys.stdin.readline
lst = []; n = int(input())
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

s = 0
for i in range(2, len(lst), 3):
    s += lst[i]

print(sum(lst) - s)