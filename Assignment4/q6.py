def Check(x,min,max):
        if x>=min and x<=max:
            return True
        else:
            return False
if Check(14,5,45):
    print("15 lies in range")
else:
    print("15 does not lie in range")
