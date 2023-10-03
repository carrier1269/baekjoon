# 실패 1

# import sys;input=sys.stdin.readline
# n=int(input()); log_name, log_enter, leave_list, result_list=[], [], [], []
# for _ in range(n):
#     name, enter = map(str, input().rstrip().split())

#     log_name.append(name)
#     log_enter.append(enter)

# for i in range(len(log_enter)):
#     if log_enter[i] == "leave":
#         leave_list.append(log_name[i])
    
# for j in log_name:
#     if j not in leave_list:
#         result_list.append(j)

# result_list.sort(reverse=True)

# for k in result_list:
#     print(k)

# 실패 2 -> 리스트를 문자열로 바꿔 풀었는데 이것도 느린가봄..

# import sys;input=sys.stdin.readline
# n=int(input());name_string = "";leave_name_string = ""
# for _ in range(n):
#     name, enter = map(str, input().rstrip().split())

#     name_string += (name + " ")

#     if enter == "leave":
#         leave_name_string += (name + " ")

# name_set = set(name_string.split())

# rs = []
# for i in name_set:
#     if i not in leave_name_string:
#         rs.append(i.rstrip())

# rs.sort(reverse=True)

# for j in rs:
#     print(j)

# 3 -> 리스트, 문자열 대신에 딕셔너리 사용

import sys;input=sys.stdin.readline
n=int(input());temp_dict={}
for _ in range(n):
    name, enter = map(str, input().rstrip().split())

    temp_dict[name] = enter

result = []

for a, b in temp_dict.items():
    if b != "leave":
        result.append(a)
result.sort(reverse=True)
for i in result:
    print(i)