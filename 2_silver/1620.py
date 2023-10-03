import sys;input=sys.stdin.readline
n, m = map(int, input().split())
cnt, mon_dict = 1, {}
for _ in range(n):
    string_input = str(input().rstrip())
    mon_dict[cnt] = string_input
    mon_dict[string_input] = cnt
    cnt += 1
for _ in range(m):
    pocketmon_input = input().rstrip()
    if pocketmon_input.isdigit():print(mon_dict[int(pocketmon_input)])
    else:print(mon_dict[pocketmon_input])