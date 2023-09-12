import sys

input = sys.stdin.readline

two = "ABC"
three = "DEF"
four = "GHI"
five = "JKL"
six = "MNO"
seven = "PQRS"
eight = "TUV"
nine = "WXYZ"
telephone_list =[two, three, four, five, six, seven, eight, nine]

string = str(input())

time = 0

for i in string:
    for j in telephone_list:
        if i in j:
            time += telephone_list.index(j) + 3
        else:
            continue

print(time)