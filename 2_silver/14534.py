import sys;input=sys.stdin.readline
from itertools import permutations
for i in range(int(input())):
    st = str(input().rstrip())

    print("Case # {}:".format(i+1))
    for i in permutations(st, len(st)):
        print(''.join(i))