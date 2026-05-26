def caseCounter(inp):
    upCase=0
    lwCase=0
    for x in inp:
        if x.isupper():
            upCase+=1
        else:
            lwCase+=1
    print(f"Uppercase letter:{upCase} and Lowercase letter:{lwCase}")
caseCounter("AAyuSh")
