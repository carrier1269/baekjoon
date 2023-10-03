import sys;input=sys.stdin.readline
string,temp_list= str(input().rstrip()),[]
for i in range(len(string)):
    for j in range(len(string)):
        if string[i:j+1] != '':temp_list.append(string[i:j+1])
print(len(set(temp_list)))