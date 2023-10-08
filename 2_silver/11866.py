# import sys;input=sys.stdin.readline
# n,k=map(int, input().split());rs=[]
# from collections import deque
# t = deque()
# for i in range(1, n+1):
#     t.append(i)
# cnt = 1
# while(True):
#     if t:
#         if cnt == 3:
#             rs.append(t.popleft())
#             cnt = 1
#         else:
#             t.append(t.popleft())

#             cnt += 1
#     else:
#         break
    
# print("<{}>".format(", ".join(map(str, rs))))

import sys;input=sys.stdin.readline
from collections import deque
n,k=map(int, input().split());rs,t,cnt=[],deque(),1
for i in range(1, n+1):t.append(i)
while(True):
    if t:
        if cnt == k:rs.append(t.popleft());cnt = 1
        else:t.append(t.popleft());cnt += 1
    else:break
print("<{}>".format(", ".join(map(str, rs))))