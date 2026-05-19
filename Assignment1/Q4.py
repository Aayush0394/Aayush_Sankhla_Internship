name = input("Enter student name: ")
Class = input("Enter your class: ")
t=0
for i in range(1,6):
    k = int(input(f"Enter your {i} subject marks: "))
    t = t+k
per = ((t/500)*100)
print("Name: ",name)
print("Class: ",Class)
print(F"Percentage:{per}%")
if (per>=60):
    print("Grade: A")
elif ((per>=50 & per<60)):
    print("Grad: B")
elif ((per>=40 & per<50)):
    print("Grad: C")
elif ((per>=33 & per<40)):
    print("Grade: D")
else:
    print("Fail")
