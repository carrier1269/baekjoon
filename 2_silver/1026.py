import sys;input=sys.stdin.readline
n=int(input())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    lesser, equal, better = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            better.append(num)
        else:
            equal.append(num)

    return quick_sort(lesser) + equal + quick_sort(better)

def reverse_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]

    lesser, equal, better = [], [], []

    for num in arr:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            better.append(num)
        else:
            equal.append(num)

    return reverse_quick_sort(better) + equal + reverse_quick_sort(lesser)

a_list = quick_sort(a_list)

b_list = reverse_quick_sort(b_list)

sum = 0

for i in range(n):
    sum += (a_list[i] * b_list[i])

print(sum)