import sys;input=sys.stdin.readline
n, number, cnt= int(input()), 665, 0

while(True):
    number+=1
    if str(number).count("666") >= 1:
        cnt += 1
        if cnt == n:print(number);break