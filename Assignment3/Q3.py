num = int(input("Enter a number: "))
T1 = num
T2 = 0

while num > 0:
    digit = num%10
    T2 = T2*10+digit
    num = num//10   
if T1 == T2:
    print(T1, "is a Palindrome Number")
else:
    print(T2, "is not a Palindrome Number")
