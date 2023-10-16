import sys;input=sys.stdin.readline
from itertools import combinations
import math
n=int(input())
num_list=list(map(int,input().split()))
prime_list=[]
lcm_list=[]

for i in num_list:
    st = True
    for a in range(2, int(i**0.5)+1):
        if i % a == 0:
            st = False
            break

    if st != False:
        prime_list.append(i)

def lcm(a, b):
    return a // math.gcd(a, b) * b

if prime_list:
    rs = prime_list[0]
    for j in range(1, len(prime_list)):
        rs = lcm(rs, prime_list[j])

    print(rs)
else:
    print(-1)