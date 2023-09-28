# n=int(input());temp_list=[int(input())for _ in range(n)]

# def quick_sort(arr):
#     if len(arr) <= 1:return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
    
#     for num in arr:
#         if num < pivot:lesser_arr.append(num)
#         elif num > pivot:greater_arr.append(num)
#         else:equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# for i in range(n):
#     print(quick_sort(temp_list)[i])

# 입력 메모리 제한으로 인해 값을 저장하는 배열을 사용하지 않고
# 배열의 인덱스를 사용하여 계수 정렬을 한다.

import sys;input=sys.stdin.readline
arr, n=[0]*10001,int(input())
for _ in range(n):arr[int(input())] += 1
for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)