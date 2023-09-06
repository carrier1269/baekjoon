import sys

input = sys.stdin.readline

a = int(input())

b = a / 4

string = "long " * int(b)

print(string + "int")