import sys;input=sys.stdin.readline
n = int(input())
road = list(map(int,input().split()))
cost = list(map(int,input().split()))

rs = 0
m = cost[0]
for i in range(n-1):
    if cost[i] < m:
        m = cost[i]
    rs += (m * road[i])

print(rs)