import sys;input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)

def func(num):
    if dp[num]:
        return dp[num]
    if num == 0:
        dp[num] = 1
        return 1
    elif num == 1:
        dp[num] = 1
        return 1
    elif num == 2:
        dp[num] = 2
        return 2
    elif num == 3:
        dp[num] = 5
        return 5
    else:
        sum = 0

        for i in range(num):
            sum += func(i) * func(num - i - 1)

        dp[num] = sum
        return sum
    
print(func(n))

    