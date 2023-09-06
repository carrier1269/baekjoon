import sys

def input():
    return sys.stdin.readline()

h, m = map(int, input().split())

time = h * 60 + m

fix_time = time - 45

fix_h = fix_time // 60

fix_m = fix_time - (fix_h * 60)

if fix_h < 0:
    fix_h = 23

print(f'{fix_h} {fix_m}')
