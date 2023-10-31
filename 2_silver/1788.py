import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

dp = [0] * (abs(N)+1)

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
        dp[num] = (Fibo(num-1) + Fibo(num-2)) % 1000000000
        return Fibo(num-1) + Fibo(num-2) % 1000000000


if N > 0:
    print(1)
    print(Fibo(N))
elif N < 0:
    print(-1)
    print(Fibo(abs(N)))
else:
    print(0)
    print(Fibo(N))

