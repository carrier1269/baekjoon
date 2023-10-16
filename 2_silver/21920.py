import sys;input=sys.stdin.readline;import math
n=int(input())
temp_list=[]
num_list=list(map(int,input().split()))
X = int(input())
def lcm(a, b):
    return a // math.gcd(a, b) * b
for i in num_list:
    if math.gcd(i, X) == 1 and lcm(i, X) == i * X:
        temp_list.append(i)
print(sum(temp_list)/len(temp_list))