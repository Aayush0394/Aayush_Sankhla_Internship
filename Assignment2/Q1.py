#Dictionary
student = {"name": "Aayush","age": 20,"course": "BTech"}
print("Student Details:")
print(student,type(student))
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
student1 = {"name": "Aayush","age": 20,"course": "BTech","personal":{"Address":"Jaipur","Father Name":"Vijay"}}
print(student1)
print(student1["personal"]["Address"])
student1["Collage"] = "SKIT"
print(student1)
del(student["course"])
print(student)
print("\n")

#Tuple
T1 = ("Red", "Green", "Blue")
print("1. Tuple Elements:")
print(T1)
print("First Color:", T1[0])
print("Second Color:", T1[1])

T2 = ("Black","Yellow","Brown")
print("2. Tuple Elements:")
print(T2)
print("Concatenation Tuple:",T1+T2)
T3 = (T1,T2)
print("Nested Tuple:",T3)
T4 = (T1)*3
print("Replication in tuple: ",T4)
print("T1 Length: ",len(T1))

T5 = (23,56,1,55,345,3,1,1)
print(T5)
print("Minimum :",min(T5))
print("Maximum: ",max(T5))
print("Count of 1: ",T5.count(1))
print("Index Finding: ",T5.index(55))
print("Sum of all:",sum(T5))
print("\n")


#Set
s1 = {1, 2, 3, 4, 5}
print("Set Elements:")
print(s1)
s1.add(6)
print("After Adding 6:")
print(s1)
print("Set s1: ",s1)
s2 = {90,67,45,34,69,5,3}
print("Set s2 :",s2)
print("Union of s1 & s2: ",s1.union(s2))
print("Intersection: ",s1.intersection(s2))
print("Difference: ",s1-s2)





