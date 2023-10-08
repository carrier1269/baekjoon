import sys;input=sys.stdin.readline

while(True):
    lst = []
    state = False
    string = str(input().rstrip())

    if string == '.':
        break
    for i in string: 
        if i == '(':
            lst.append(i)
        elif i == ')':
            if lst and lst[-1] == '(':
                lst.pop()
            else:
                state = True
                break
        if i == '[':
            lst.append(i)
        elif i == ']':
            if lst and lst[-1] == '[':
                lst.pop()
            else:
                state = True
                break

    if state == True:
        print("no")
        continue
    if lst:
        print("no")
    else:
        print("yes")