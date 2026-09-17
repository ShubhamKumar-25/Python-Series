# print("Hey Rohan Gupta")

# print("Kya hal hai bhai log")

# name = "Rohan Kumar"
# print(name)

# marks = 98
# print(marks)

# num = int(input("Enter your number : "))
# print("Your number is :",num)

age = int(input("Enter your age: "))

# age = int(age)+1
print(type(age))

name = str(input("Enter your name :"))
print(type(name))


def add_numbers(a, b):
    result = a + b
    return result

# Calling the function
total = add_numbers(5, 10)
print(total)  # Output: 15



def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Shubham"))           # Output: Hello, Shubham!
print(greet("Shubham", "Welcome")) # Output: Welcome, Shubham!