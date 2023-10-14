import sys;input=sys.stdin.readline


for _ in range(int(input())):
    n = int(input())

    dp = [0] * (n+1)

    def triangle(num):
        if dp[num]:
            return dp[num]
        else:
            if num == 1:
                dp[num] == 1
                return 1
            if num == 2:
                dp[num] == 1
                return 1
            if num == 3:
                dp[num] == 1
                return 1
            if num == 4:
                dp[num] == 1
                return 2
            if num == 5:
                dp[num] == 2
                return 2
            else:
                dp[num] = triangle(num-1) + triangle(num-5)
                return triangle(num-1) + triangle(num-5)
            
    print(triangle(n))