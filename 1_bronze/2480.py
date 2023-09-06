import sys

input = sys.stdin.readline()

a, b, c = map(int, input.split())

if a == b and b == c:
    print(10000 + a * 1000)
elif a == b or b == c or a == c:
    if a == b:
        print(1000 + a * 100)
    if b == c:
        print(1000 + b * 100)
    if a == c:
        print(1000 + c * 100)
elif a != b and b != c and a != c:
    dice_list = []
    dice_list.append(a)
    dice_list.append(b)
    dice_list.append(c)

    dice_list.sort()
    
    print(dice_list[-1] * 100)