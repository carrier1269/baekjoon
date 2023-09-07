import sys

input = sys.stdin.readline

lst = []

for _ in range(10):
    a = int(input())
    
    lst.append(a % 42)

count = 0

for i in range(len(lst)):
    if lst[i] not in lst[i+1 : ]:
        count += 1

print(count)