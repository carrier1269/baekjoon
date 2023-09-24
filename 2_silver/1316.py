import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    string = str(input())

    for j in range(len(string)):
        try:
            if string[j] == string[j + 1]:
                continue  
            elif string[j] in string[j + 1 :]:
                n -= 1
                break
        except:
            pass

print(n)
