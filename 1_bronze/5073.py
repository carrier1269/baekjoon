import sys;input=sys.stdin.readline
while(True):
    temp_list = list(map(int, input().split()))
    a,b,c = map(int, temp_list)
    temp_list.sort()
    if a==0 and b==0 and c==0:
        break
    elif temp_list[-1] >= sum(temp_list[0:2]):
        print("Invalid")
    elif a==b and b==c:
        print("Equilateral")
    elif a==b or a==c or b==c:
        print("Isosceles")
    else:
        print("Scalene")