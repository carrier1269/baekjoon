import sys;input=sys.stdin.readline
n=int(input()); log_name, log_enter, leave_list, result_list=[], [], [], []
for _ in range(n):
    name, enter = map(str, input().rstrip().split())

    log_name.append(name)
    log_enter.append(enter)

for i in range(len(log_enter)):
    if log_enter[i] == "leave":
        leave_list.append(log_name[i])
    
for j in log_name:
    if j not in leave_list:
        result_list.append(j)

result_list.sort(reverse=True)

for k in result_list:
    print(k)