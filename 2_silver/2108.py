# import sys;input=sys.stdin.readline
# import bisect
# n=int(input())
# temp_list = []
# for _ in range(n):
#     temp_list.append(int(input()))


# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]

#     lesser, equal, better = [], [], []

#     for i in arr:
#         if i < pivot:
#             lesser.append(i)
#         elif i > pivot:
#             better.append(i)
#         else:
#             equal.append(i)
        
#     return quick_sort(lesser) + equal + quick_sort(better)

# temp_list = quick_sort(temp_list)

# print(round(sum(temp_list)/len(temp_list)))

# print(temp_list[len(temp_list)//2])

# cnt = []
# for i in temp_list:
#     cnt.append(temp_list.count(i))

# cn = 0
# dup = []
# for j in range(len(cnt)):
#     if max(cnt) == cnt[j]:
#         cn += 1
#         dup.append(temp_list[j])
# dup.sort()

# if cn != 1:
#     print(dup[1])
# else:
#     print(temp_list[bisect.bisect_left(cnt, max(cnt))])
# print(max(temp_list) - min(temp_list))

import sys;input=sys.stdin.readline;n=int(input());dt = {};tmp_lst = []
for _ in range(n):
    a = int(input())
    tmp_lst.append(a)
    try:
        # a의 idx에 value가 있으면 cnt값 추가
        if dt[a] >= 1:
            dt[a] += 1
        # a의 idx에 value가 없다면 1값 생성
    except:
        dt[a] = 1

print(round(sum(tmp_lst) / len(tmp_lst)))

tmp_lst.sort()
print(tmp_lst[len(tmp_lst)//2])

# idx의 value들 중에 count한 값이 제일 큰것
max_cnt = max(dt.values())

dup = []


for k, v in dt.items():
    # v -> value의 값이 결국 idx 넘버 count 값인데,
    # count한 값이 max count값이랑 같다면
    if max_cnt == v:
        # dup 리스트에 추가하는데,
        # max count값이 count값과 똑같은 값이 또 있다면
        # 추가로 판별하기 위해서 리스트에 추가
        dup.append(k)

dup.sort()
try:
    print(dup[1])
except:
    print(dup[0])

print(max(tmp_lst) - min(tmp_lst))