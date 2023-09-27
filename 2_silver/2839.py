# import sys;input=sys.stdin.readline;
# n,cnt,temp_list=int(input()),0,[]
# for i in range(0, 1001):
#     for j in range(0, 1667):
#         if i * 5 + j * 3 == n:temp_list.append(i+j)
# if len(temp_list) == 0:print(-1)
# else:print(min(temp_list))

import sys;n,c=int(sys.stdin.readline()),0
while n>=0:
    if n%5==0:print(c+n//5);break
    n-=3;c+=1
else:print(-1)