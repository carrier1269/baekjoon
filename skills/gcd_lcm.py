import math

def lcm(a,b):
    return a // math.gcd(a, b) * b

def gcd(a,b):
    return math.gcd(a, b)

# N개 수의 최소공배수 lcm

num_list = []
if num_list:
    rs = num_list[0]
    for j in range(1, len(num_list)):
        rs = lcm(rs, num_list[j])