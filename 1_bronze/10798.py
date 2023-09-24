import sys

input = sys.stdin.readline

lst = []

max_column_length = 0

for _ in range(5):
    string = str(input().rstrip())

    lst.append(string)

    if len(string) > max_column_length:
        max_column_length = len(string)

max_row_length = len(lst)

max_length = 0

if max_row_length > max_column_length:
    max_length = max_row_length
else:
    max_length = max_column_length

result_str = ""

for i in range(max_length):
    for j in range(max_length):
        try:
            result_str += lst[j][i]
        except:
            continue

print(result_str)