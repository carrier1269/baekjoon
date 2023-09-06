A = int(input())
B, C, D = map(int, input())

print(f"{A*D}\n{A*C}\n{A*B}\n{A*(B*100+C*10+D)}")