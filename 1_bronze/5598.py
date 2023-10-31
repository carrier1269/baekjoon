import sys;input=sys.stdin.readline
alpha = list('X Y Z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split())

a = str(input().rstrip())

rs = ''

for i in a:
    if alpha.index(i) > 3:
        rs = rs + alpha[(alpha.index(i) - 3)]
    else:
        rs = rs + alpha[(alpha.index(i) + 23)]

print(rs)