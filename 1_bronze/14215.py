import sys;input=sys.stdin.readline
temp_list=list(map(int,input().split()));temp_list.sort()
max_length_of_triangle=0
if temp_list.count(temp_list[0]) == 3: 
    print(sum(temp_list))
elif max(temp_list) < sum(temp_list[0:2]):
    print(sum(temp_list))
else: 
    max_length_of_triangle=sum(temp_list[0:2])-1
    print(max_length_of_triangle+sum(temp_list[0:2]))