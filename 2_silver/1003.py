import sys;input=sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())


    zero_count, one_count = 0, 0

    def Fibo(num):
        global zero_count, one_count

        if num == 0:
            zero_count += 1
            return 0
        elif num == 1:
            one_count += 1
            return 1
        else:
            return Fibo(num-1) + Fibo(num-2)
    
    Fibo(N)
    print(zero_count, one_count)
        
