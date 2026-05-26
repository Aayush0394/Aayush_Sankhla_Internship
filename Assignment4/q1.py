def maxOf3(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            print("Max:",n1)
        else:
            print("Max:",n3)
    else:
        if n2>n3:
            print("Max:",n2)
        else:
            print("Max:",n3)
maxOf3(2,10,4)
