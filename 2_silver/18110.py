# version 1

# import sys;input=sys.stdin.readline
# n=int(input());l=[]

# for _ in range(n):
#     l.append(int(input()))

# def round_num(num):
#     if int(str(num).split('.')[1][0]) >= 5:
#         return int(num) + 1
#     else:
#         return int(num)
    
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]

#     lesser, equal, better = [], [], []

#     for num in arr:
#         if num < pivot:
#             lesser.append(num)
#         elif num > pivot:
#             better.append(num)
#         else:
#             equal.append(num)

#     return quick_sort(lesser) + equal + quick_sort(better)
    
# cut=round_num(n*0.15)

# l = quick_sort(l)

# sumz, cnt = 0, 0
# for i in range(cut,len(l)-cut):
#     sumz += l[i]
#     cnt += 1

# if n == 0:
#     print(0)
# else:
#     print(round_num(sumz/cnt))

# version 2

# import sys;input=sys.stdin.readline
# n=int(input());l=[]

# for _ in range(n):
#     l.append(int(input()))

# def round_num(num):
#     if int(str(num).split('.')[1][0]) >= 5:
#         return int(num) + 1
#     else:
#         return int(num)
    
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr)//2]

#     lesser, equal, better = [], [], []

#     for num in arr:
#         if num < pivot:
#             lesser.append(num)
#         elif num > pivot:
#             better.append(num)
#         else:
#             equal.append(num)

#     return quick_sort(lesser) + equal + quick_sort(better)
    
# cut=round_num(n*0.15)

# l = quick_sort(l)

# if n == 0:
#     print(0)
# else:
#     print(round_num(sum(l[cut:n-cut])/(n-2*cut)))


import sys;input=sys.stdin.readline;n,l=int(input()),[]
for _ in range(n):l.append(int(input()))
def R(a):
    if int(str(a).split('.')[1][0])>=5:return int(a)+1
    else:return int(a)
c=R(n*0.15);l.sort()
if n==0:print(0)
else:print(R(sum(l[c:n-c])/(n-2*c)))