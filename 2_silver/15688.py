import sys;input=sys.stdin.readline

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr)//2]

    lesser, equal, better = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            better.append(num)
        else:
            equal.append(num)

    return quick_sort(lesser) + equal + quick_sort(better)

num_list = [int(input()) for _ in range(int(input()))]

for i in quick_sort(num_list):
    print(i)