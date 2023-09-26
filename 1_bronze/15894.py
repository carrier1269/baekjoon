import sys

input = sys.stdin.readline

n = int(input())

def pattern1(count):
    return count - 1

def pattern2(count):
    return count

def pattern3(count):
    return 2*(count-1)

def sum_pattern(count):
    return 3 + pattern1(count) + pattern2(count) + pattern3(count)


if n != 1:
    print(sum_pattern(n))
else:
    print(4)