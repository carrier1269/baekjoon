import sys, math; input=sys.stdin.readline
t=[]
for _ in range(2):
    a, b = map(int,input().split())
    t.append([a,b])
x, y = t[0][0]*t[1][1]+t[0][1]*t[1][0],t[0][1]*t[1][1]
k = math.gcd(x,y)
print('{} {}'.format(x//k,y//k))

# import sys, math; input,t=sys.stdin.readline,[]
# for _ in range(2):
#     a, b = map(int,input().split());t.append([a,b])
# x, y = t[0][0]*t[1][1]+t[0][1]*t[1][0],t[0][1]*t[1][1]
# print('{} {}'.format(x//math.gcd(x,y),y//math.gcd(x,y)))