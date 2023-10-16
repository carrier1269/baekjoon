from itertools import combinations;import math
n = int(input())
for _ in range(n):
    a = list(map(int,input().split()))
    del a[0];sum = 0
    for i in list(combinations(a,2)):
        sum += math.gcd(i[0],i[1])  
    print(sum)