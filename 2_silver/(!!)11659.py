import sys;input=sys.stdin.readline
n, m = map(int,input().split())
temp_list = list(map(int,input().split()))

def prefix_Sum(arr):
    prefixSum = [0]*(b-a+1)
    prefixSum[0] = arr[0]
    for i in range(1,b-a+1):
        prefixSum[i] = prefixSum[i-1] + arr[i]    
    
    return prefixSum[-1]

for _ in range(m):
    a, b = map(int,input().split())

    sum_range = temp_list[a-1:b]

    print(prefix_Sum(sum_range))