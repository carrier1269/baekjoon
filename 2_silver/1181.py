import sys;input=sys.stdin.readline
n=int(input())
temp_list=[]
for _ in range(n):
    temp_list.append(input().rstrip())
temp_list = list(set(temp_list))
temp_list.sort()

def length_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]

    lesser, equal, greater = [], [], []

    for str in arr:
        if len(str) < len(pivot):
            lesser.append(str)
        elif len(str) > len(pivot):
            greater.append(str)
        else:
            equal.append(str)

    return length_sort(lesser) + equal + length_sort(greater)

temp_list = length_sort(temp_list)

for i in temp_list:
    print(i)