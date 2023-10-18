import sys; input=sys.stdin.readline
t=int(input())
for x in range(t):
    tmp = list(map(int,input().split()))

    sum = 0

    for i in tmp:
        if i % 2 != 0:
             sum += i
    
    print('#{} {}'.format(x+1, sum))