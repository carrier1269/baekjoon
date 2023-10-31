A, P = map(int, input().split())

visted = [A]
def dfs(A, P, visted):
    aa = list(map(int, str(A)))
    for i in range(len(aa)):
        aa[i] = aa[i]**P
    s = sum(aa)
    if s not in visted:
        visted.append(s)
        dfs(s, P, visted)
    else:
        k = visted.index(s)
        return print(len(visted[:k])) 

dfs(A,P,visted)