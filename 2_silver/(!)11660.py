import sys;input=sys.stdin.readline
N, M = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(N)]


# dp로 해결

dp = [[0 for _ in range(N+1)]*(N+1)]

def array_sum(arr, x1, y1, x2, y2):
    
    for a in range(1, N+1):
        for b in range(1, N+1):
            dp[a][b] = dp[x2][y2] - dp[x1-1][y2]


    # sum = 0
    # for i in range(x1-1,x2):
    #     for j in range(y1-1,y2):
    #         sum += arr[i][j]
    # return sum

for _ in range(M):
    X1, Y1, X2, Y2 = map(int,input().split())
    print(array_sum(array, X1, Y1, X2, Y2))