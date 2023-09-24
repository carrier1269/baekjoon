import sys

input = sys.stdin.readline

def pattern1(number):
    return 2 * number - 1

def pattern2(number):
    return number - 2

def pattern_make(number):
    return 2 * pattern1(number) + 2 * pattern2(number)

a = int(input())

count = 1

before_num = 1

while(True):
    if a != 1:
        count += 1

        number_count = pattern_make(count)

        if a > before_num and a <= before_num + number_count:
            print(count)
            break
        else:
            before_num += number_count
    else:
        print(1)
        break