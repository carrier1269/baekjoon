import sys; input=sys.stdin.readline;sys.setrecursionlimit(10**6)
n=int(input())

d = [0] * 100000

def Fibonacci(num):
    if num == 1: return 1
    if num == 2: return 1
    if d[num] != 0: return d[num]
    else: d[num] = Fibonacci(num-1) + Fibonacci(num-2)
    return Fibonacci(num-1) + Fibonacci(num-2)

print(Fibonacci(n))