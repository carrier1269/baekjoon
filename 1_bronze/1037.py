import sys;input=sys.stdin.readline
n=int(input())
s=list(map(int,input().split()))
if n == 1:
    print(s[0]**2)
else:
    print(min(s)*max(s))