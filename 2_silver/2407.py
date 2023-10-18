import sys;input=sys.stdin.readline
sys.setrecursionlimit(10**8)
n,m = map(int,input().split())
dp=[0]*(n+1)
def factorial(num):
    if dp[num]:
        return dp[num]
    if num == 0:
        dp[num] = 1
        return 1
    elif num == 1:
        dp[num] = 1
        return 1
    else:
        dp[num] = factorial(num - 1) * num
        return factorial(num - 1) * num
    

print(factorial(n)//(factorial(m)*factorial(n-m)))

# /가 아닌 //를 사용한 이유는
# 파이썬에서 //, int 형 결과값을 얻으면 크기에 구속을 받지 않으나,
# /, float 자료형 결과값은 크기에 구속을 받기 때문에
# 값이 커지면 오차가 발생한다.