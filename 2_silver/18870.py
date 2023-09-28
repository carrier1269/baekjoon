# import sys;input=sys.stdin.readline
# n=int(input())
# temp_list=list(map(int,input().split()))
# result_list = [0] * n
# cp_list=list(set(temp_list.copy()))
# cp_list.sort()
# cnt = 0
# for i in cp_list:
#     for j in range(len(temp_list)):
#         if temp_list[j] == i:
#             result_list[j] += cnt
#             if i in temp_list[j+1:]:
#                 continue
#             else:
#                 cnt += 1
# print(*result_list)

import sys;input=sys.stdin.readline;import bisect
n=int(input());temp_list=list(map(int,input().split()))
sort_list=sorted(list(set(temp_list)))
# print(" ".join(str(sort_list.index(i)) for i in temp_list))
print(" ".join(str(bisect.bisect_left(sort_list, i)) for i in temp_list))
