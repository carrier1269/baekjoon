import sys; input=sys.stdin.readline
n=int(input())

d = [0] * 100

def Fibonacci(num):
    if num == 1: return 1
    if num == 2: return 1
    if d[num] != 0: return d[num]
    else: d[num] = Fibonacci(num-1) + Fibonacci(num-2)
    return Fibonacci(num-1) + Fibonacci(num-2)


a = Fibonacci(n)

cnt = 0 
for i in d:
    if i != 0:
        cnt += 1
print(a, cnt)