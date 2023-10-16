import sys;input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a = int(input())
    state = True
    
    while(state):
        if a >= 2:
            st = True
            
            for i in range(2, int(a**0.5)+1):
                if a % i == 0:
                    st = False
                    break
            if st != False:
                print(a)
                state = False

            a += 1
        else:
            a += 1