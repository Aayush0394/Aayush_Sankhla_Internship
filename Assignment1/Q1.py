name = input("Enter student name: ")
Class = input("Enter your class: ")
t=0
for i in range(1,6):
    k = int(input(f"Enter your {i} subject marks: "))
    t = t+k

print("Name: ",name)
print("Class: ",Class)
print(F"Percentage:{((t/500)*100)}%")
