import sys

input = sys.stdin.readline

a, b = map(str, input().split())

new_a = a[::-1]
new_b = b[::-1]

if new_a < new_b:
    print(new_b)
else:
    print(new_a)