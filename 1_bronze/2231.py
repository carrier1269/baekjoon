import sys;input=sys.stdin.readline
def pattern(number):
    if number == 0:
        return number
    else:
        return number + sum(map(int,str(number)))
    
a = int(input())
num = 0
while(True):
    rs = pattern(num)
    if num > a:
        print(0)
        break
    elif rs == a:
        print(num)
        break
    else:
        num += 1