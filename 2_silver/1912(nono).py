n=int(input())

num = list(map(int,input().split()))

def lcs(nums):
    n = len(nums)
    table = [0 for _ in range(n)]
    table[0] = nums[0]
    for i in range(1, n):
        table[i] = max(table[i-1]+nums[i],nums[i])

    print(table)

    return max(table)

print(lcs(num))