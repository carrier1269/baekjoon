# import sys;input=sys.stdin.readline
# a,b,c,d,e,f=map(int,input().split())
# try:
#     div_num=-(d/a)
#     y=(div_num*c+f)/(div_num*b+e);x=(c-b*y)/a
#     print("{} {}".format(int(x),int(y)))
# except:
#     print("{} {}".format(0,0))

import sys;input=sys.stdin.readline
a,b,c,d,e,f=map(int,input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y==c and d*x+e*y==f:
            print("{} {}".format(x,y))