import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N=int(input())
lst=list(map(int,input().split()))
lst.sort()

sum_found = []

def max_find(arr, i, j):
    if i < j:
        sum_found.append(lst[i] + lst[j])
        return max_find(arr, i+1, j-1)
    if i == j:
        sum_found.append(lst[i])
    else:
        return

if len(lst) % 2 == 0:
    max_find(lst, 0, len(lst) - 1)
else:
    max_find(lst[:len(lst)-1], 0, len(lst) - 2)
    sum_found.append(lst[-1])
print(max(sum_found))