# import sys

# input = sys.stdin.readline

# num = int(input())

# for i in range(2 * num):
#     if i == 0:
#         continue
#     elif i <= num:
#         print(" " * (num - i) + "*" * (2 * i - 1))
#     else:
#         j = (num * 2) - i
#         i -= num
#         print(" " * i + "*" * (2 * j - 1))

import sys;input=sys.stdin.readline;n=int(input())
for i in range(1, 2*n+1):
    if i <= n:print(' '*(n-i)+'*'*(2*i-1))
    else:print(' '*(i-n)+'*'*(4*n-2*i-1))