n=int(input())
f=[0,1]
rs = 0
if n == 0: print(0)
elif n == 1: print(1)
else:
    for i in range(1,n):
        rs = f[0] + f[1]
        f[0],f[1] = f[1],rs
    print(rs)