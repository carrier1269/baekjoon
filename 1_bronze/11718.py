import sys

input = sys.stdin.readline

input_list = []

while(True):
    a = str(input().rstrip())

    if len(a) > 0:
        input_list.append(a)
    else:
        break

for i in input_list:
    print(i)
