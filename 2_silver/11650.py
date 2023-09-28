# import sys;input=sys.stdin.readline
# temp_list = [[] for _ in range(200001)]

# def quick_sort(arr):
#     if len(arr) <= 1:return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
    
#     for num in arr:
#         if num < pivot:lesser_arr.append(num)
#         elif num > pivot:greater_arr.append(num)
#         else:equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# for _ in range(int(input())):
#     x, y = map(int, input().split())
#     if x >= 0:
#         temp_list[x].append(y)
#     else:
#         temp_list[-x+100000].append(y)
# for a in range(len(temp_list)-1, 100000, -1):
#     if len(temp_list[a]) != 0:
#         for h in range(len(temp_list[a])):
#             print("{} {}".format(-a+100000, quick_sort(temp_list[a])[h]))

# for i in range(len(temp_list)-100000):
#     if len(temp_list[i]) != 0:
#         for j in range(len(temp_list[i])):
#             print("{} {}".format(i, quick_sort(temp_list[i])[j]))

import sys; input=sys.stdin.readline
n = int(input());temp_list=[]
for _ in range(n):
    x, y = map(int, input().split())
    temp_list.append([x,y])

for i, j in sorted(temp_list):
    print(i, j)