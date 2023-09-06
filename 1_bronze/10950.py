import sys

def input():
    return sys.stdin.readline()

test_num = int(input())

for _ in range(test_num):
    a, b = map(int, input().split())

    print(a + b)