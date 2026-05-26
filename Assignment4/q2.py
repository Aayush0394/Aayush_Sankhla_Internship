def distinct(l):
    L=[]
    s=set()
    for x in l:
        s.add(x)
    for y in s:
        L.append(y)
    return L
L1=[2,3,4,2,3,5,6]
ans=distinct(L1)
print("Distinct list:",ans)
