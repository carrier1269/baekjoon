import sys;input=sys.stdin.readline
n=int(input())
lst = list(map(int,input().split()))

lst.sort(reverse=True)

p = lst[0]

for i in range(1, len(lst)):
    if p < lst[i]:
        p = lst[i] + (p / 2)
    else:
        p = p + (lst[i] / 2)

print(p)