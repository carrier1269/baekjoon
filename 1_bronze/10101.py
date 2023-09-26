import sys;input=sys.stdin.readline
temp_list = []
for i in range(3):
    temp_list.append(int(input()))
a,b,c=map(int,temp_list)
if a+b+c!=180:
    print("Error")
elif a==b and b==c:
    print("Equilateral")
elif a==b or a==c or b==c:
    print("Isosceles")
else:
    print("Scalene")