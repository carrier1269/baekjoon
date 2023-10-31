import sys;input=sys.stdin.readline
n = int(input())
wine = [int(input()) for _ in range(n)]

dp = [0] * (n)

# dp 0번째는 와인 0번째
dp[0] = wine[0]

# dp 1번째는 와인 0 + 와인 1
if n > 1:
    dp[1] = wine[0] + wine[1]

# dp 2번째는 와인 0+2가 될수도 있고, 와인 1+2가 될수도 있고, 지금까지 더한 이전의 최댓값 dp[1]이 될수도 있다.
if n > 2:
    dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])

for i in range(3, n+1):
    try:
        # 지금과 전을 먹었을때 + 전전전까지 최대값
        # 지금과 전전(전전까지 최대값)을 먹었을때
        # dp[2]와 같은 방식으로 현재를 먹지 않는 값이 최대가 될수도 있으니 전까지의 최대값도 계산
        dp[i] = max(wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2], dp[i - 1])
    except:
        continue

print(dp[n-1])