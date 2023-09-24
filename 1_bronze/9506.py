import sys

input = sys.stdin.readline

while(True):
    a = int(input())

    temp_list = []

    if a != -1:
        for i in range(1, a):
            if a % i == 0:
                temp_list.append(i)
        
        if a != sum(temp_list):
            print("{} is NOT perfect.".format(a))
        else:
            print("{} = {}".format(a, " + ".join(map(str, temp_list))))
    else:
        break