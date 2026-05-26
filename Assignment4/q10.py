with open("myfile.txt","r") as file:
    print(file.read())
print("____________________________")
#WRITE
with open("myfile1.txt","w") as file:
    file.write("Second file\n")
    file.write("Third line.")
#APPEND
with open("myfile1.txt","a") as file:
    file.write("Fourth line\n")
    file.write("Fifth line.")
with open("myfile1.txt","r") as file:
    data=file.read()
    print(data)
