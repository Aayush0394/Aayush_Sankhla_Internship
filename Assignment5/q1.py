import csv
data=[]
data.append(["Name","Adress","Mobile","Email"])
for i in range(1,4):
    inp=input("Enter Name,Address,Mobile,Email:")
    inp=inp.split()
    data.append(inp)
with open('data.csv','w',newline='') as file:
    writer=csv.writer(file)
    for row in data:
        writer.writerow(row)
