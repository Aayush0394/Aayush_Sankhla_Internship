def revStr(str):
    ans=""
    for x in str[::-1]:
        ans+=x
    return ans
ans=revStr(str="HELLO")
print("Reversed:",ans)
