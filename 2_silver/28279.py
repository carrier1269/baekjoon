# import sys;input=sys.stdin.readline
# from collections import deque
# n=int(input());t=deque()
# for _ in range(n):
#     a = str(input().rstrip())

#     if len(a) > 2:
#         b, c = map(int, a.split())

#         if b == 1:
#             t.appendleft(c)
#         elif b == 2:
#             t.append(c)
        
#     else:
#         a = int(a)
#         if a == 3:
#             if t:
#                 print(t.popleft())
#             else:
#                 print(-1)
#         elif a == 4:
#             if t:
#                 print(t.pop())
#             else:
#                 print(-1)
#         elif a == 5:
#             print(len(t))
#         elif a == 6:
#             if t:
#                 print(0)
#             else:
#                 print(1)
#         elif a == 7:
#             if t:
#                 print(t[0])
#             else:
#                 print(-1)
#         elif a == 8:
#             if t:
#                 print(t[-1])
#             else:
#                 print(-1)

from collections import deque
n=int(input());t=deque()
for _ in range(n):
    a = str(input().rstrip())
    if len(a) > 2:
        b, c = map(int, a.split())
        if b == 1:t.appendleft(c)
        elif b == 2:t.append(c)
    else:
        a = int(a)
        if a == 3:
            if t:print(t.popleft())
            else:print(-1)
        elif a == 4:
            if t:print(t.pop())
            else:print(-1)
        elif a == 5:print(len(t))
        elif a == 6:
            if t:print(0)
            else:print(1)
        elif a == 7:
            if t:print(t[0])
            else:print(-1)
        elif a == 8:
            if t:print(t[-1])
            else:print(-1)