import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())
# temp_list = []
# temp_list.append(x-0);temp_list.append(y-0);temp_list.append(w-x);temp_list.append(h-y)
temp_list = [x-0,y-0,w-x,h-y]
print(min(temp_list))