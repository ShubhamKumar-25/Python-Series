
# File input and output in python
file = open("Student_records.txt", 'w')

# Data write karna
file.write("Name: Shubham\n")
file.write("Course: B.Tech IT\n")
file.write("Status: Active\n")
file.close()
print("File successfully created and data written!")