import sys;input=sys.stdin.readline
n,m=map(int,input().split());cnt=0
check=set(str(input()) for _ in range(n))
for _ in range(m):
    if str(input()) in check:
        cnt += 1
print(cnt)