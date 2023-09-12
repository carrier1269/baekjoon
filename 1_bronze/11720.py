import sys

input = sys.stdin.readline

n = int(input())

num_string = str(input())

sum = 0

for i in range(n):
    sum += int(num_string[i])
    
print(sum)