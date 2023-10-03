# import sys;input=sys.stdin.readline
# n=int(input());num=1;state=True
# for _ in range(n):
#     a,b = map(int,input().split())
#     while(state):
#         if num%a==0 and num%b==0:
#             print(num)
#             state = False
#         else:
#             num+=1

#     state = True
#     num = 1

import sys, math; input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a, b = map(int,input().split())
    print((a * b) // math.gcd(a,b))