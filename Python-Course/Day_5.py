
# File input and output in python
file = open("Student_records.txt", 'w')

# Data write karna
file.write("Name: Shubham\n")
file.write("Course: B.Tech IT\n")
file.write("Status: Active\n")
file.write("Marks: 89\n")
file.write("City: Motihari\n")
file.close()
print("File successfully created and data written!")


with open("Student_records.txt", 'a') as file:
    file.write("I am fullstack software develpoer \n")
print("New Data append sucessfully")


with open("Student_records.txt", "r") as file:
    content = file.read()
    print("-----Read file--------")
    print(content)