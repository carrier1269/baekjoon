import sys;input=sys.stdin.readline;n=int(input())
for _ in range(n):
    a = int(input())
    while(True):
        st = False
        for i in range(2, a):
            if a % i == 0:
                st = True
        if st != True:
            print(a)
            break
        else:
            a += 1