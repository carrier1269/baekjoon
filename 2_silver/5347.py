import math
n=int(input())

    
def lcm(a, b):
    return a // math.gcd(a, b) * b

for _ in range(n):
    a, b = map(int,input().split())

    print(lcm(a, b))