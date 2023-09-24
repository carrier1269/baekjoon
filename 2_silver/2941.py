import sys

input = sys.stdin.readline

a = str(input())

cro_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]

for i in cro_alpha:
    a = a.replace(i, "x")

print(len(a.rstrip()))