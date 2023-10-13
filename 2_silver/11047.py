import sys;input=sys.stdin.readline
n, k = map(int,input().split()); coin = []
for _ in range(n):
    coin.append(int(input()))

coin = sorted(coin, reverse=True)

cnt = 0

for i in coin:
    if i <= k:
        cnt += k // i
        k = k % i
    if k == 0:
        break
        
print(cnt)