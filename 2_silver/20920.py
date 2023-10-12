import sys;input=sys.stdin.readline
n, m = map(int,input().split());l,d=[],{}
for _ in range(n):
    a = str(input().rstrip())

    if len(a) >= m:
        l.append(a)

def length_quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    pivot_length = arr[len(arr)//2]

    lesser, equal, better = [], [], []

    for word in arr:
        if len(word) < len(pivot_length):
            lesser.append(word)
        elif len(word) > len(pivot_length):
            better.append(word)
        else:
            equal.append(word)
        
    return length_quick_sort(lesser) + equal + length_quick_sort(better)

l = length_quick_sort(l)

print(f'lenl = {l}')

l.sort()

print(f'l = {l}')




# print(f'd={d}')

# print(max(d.values()))

# tl=[]
# for k, v in d.items():
#     tl.append("{}{}".format(v,k))

# print(tl)

# def appear_quick_sort(arr):

#     if len(arr) <= 1:
#         return arr

#     print(f'ff = {len(arr)//2}')
#     print(arr[len(arr)//2][0])
#     pivot_appear = int(arr[len(arr)//2][0])

#     lesser, equal, better = [], [], []

#     for word in arr:
#         if int(word[0]) < pivot_appear:
#             lesser.append(word)
#         elif int(word[0]) > pivot_appear:
#             better.append(word)
#         else:
#             equal.append(word)

#     return appear_quick_sort(lesser) + equal + appear_quick_sort(better)

# tlm = appear_quick_sort(tl)

# print(tlm)

# tlms = []
# for i in tlm:
#     tlms.append(i[1:])

# print(tlms)



# print(l)

# l.sort()

# print(l)
