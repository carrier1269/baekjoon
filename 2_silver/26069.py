n=int(input())
rs = set()
for _ in range(n):
    a,b=map(str,input().rstrip().split())

    if a == "ChongChong" or b == "ChongChong":
        rs.add(a);rs.add(b)
        continue

    if a in rs or b in rs:
        rs.add(a);rs.add(b)
    
print(len(rs))
    
