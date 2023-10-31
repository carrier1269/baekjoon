import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
N = int(input())

dp = [0] * (N+1)

def Fibo(num):
    if dp[num]:
        return dp[num]
    
    if num == 0:
        dp[num] = 0
        return 0
    elif num == 1:
        dp[num] = 1
        return 1
    else:
        dp[num] = (Fibo(num-1) + Fibo(num-2))
        return (Fibo(num-1) + Fibo(num-2))
    
print(Fibo(N))