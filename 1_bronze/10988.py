import sys

input = sys.stdin.readline

string = str(input().rstrip())

count = 0

for i in range(len(string)):
    if len(string) == 1:
        print(1)
        break
    elif string[i] == string[len(string) - i - 1]:
        if len(string) % 2 == 0:
            count += 1
            if len(string) / 2 - count == 0:
                print(1)
                break
        else:
            count += 1
            if (len(string) - 1) / 2 - count == 0:
                print(1)
                break
        continue
    else:
        print(0)
        break
