import sys;input=sys.stdin.readline
n,m=map(int,input().split());temp_list=list(map(int,input().split()))
temp_list.sort()
result = 0
for i in temp_list:
    for j in temp_list:
        for k in temp_list:
            if i != j and i != k and j != k:
                if i + j + k <= m and i + j + k > result:
                    result = i + j + k

print(result)