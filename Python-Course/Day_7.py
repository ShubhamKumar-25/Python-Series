# # reviosn

# age = 25
# print(age)

# price = 99.99
# print(price)

# name = "Rohan Gupta"
# print(name)

# is_active = True
# print(is_active)



# marks = 98

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# else:
#     print("Grade C")


# # range(start, stop, step) -> range(5) generates numbers 0 to 4
# for i in range(5):
#     print(i)


# count = 0
# while count < 3:
#     print("Count is:", count)
#     count += 1




# # Processing JSON-like API data using List of Dicts
# students = [
#     {"id": 101, "name": "Aman", "marks": 88},
#     {"id": 102, "name": "Priya", "marks": 95}
# ]
# print(students[1]["name"])
# print(students)

# raw_labels = ["cat", "dog", "cat", "bird", "dog"]
# unique_labels = set(raw_labels) 
# print(unique_labels)



# # Standard loop
# squares = []
# for x in range(10):
#     squares.append(x**2)

# # List Comprehension
# squares = [x**2 for x in range(10)]
# print(squares)


# class Person:
#     def __init__(self):
#         self.name = "Rohan Gupta"
#         self.age = 25
#         self.city = "New Delhi"

# Person1 = Person()
# print(Person1.name)
# print(Person1.age)
# print(Person1.city)
# del Person1.age
# # print(Person1.age)  # This will raise an AttributeError since 'age' has been deleted

# class Account:
#     def __init__(self, account_number, account_password):
#         self.account_number = account_number
#         self.__account_password = account_password  # Private attribute
#         self.__account_balance = 0.0  # Private attribute

#     def reset_pass(self, new_password):
#         self.__account_password = new_password
# A1 = Account("123456789", "securepassword")
# print(A1.account_number)  # This will work
# # print(A1.__account_password)  # This will raise an AttributeError since '__account_password' is private
# A1.reset_pass("newsecurepassword")  # This will work


# inheritance
# class Animal:
#     @staticmethod
#     def make_sound():
#         return "Some generic animal sound"

#     @staticmethod
#     def eat():
#         return "Animal is eating"

#     @staticmethod
#     def sleep():
#         return "Animal is sleeping"

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

# A1 = Dog("Buddy")
# print(A1.name) 
# print(A1.make_sound())  # Inherited method
# print(A1.eat())
# print(A1.sleep())

# single inheritance -> Now we can create simple single inheritance example. 
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start_engine(self):
#         return f"{self.brand} {self.model} engine started."

#     def stop_engine(self):
#         return f"{self.brand} {self.model} engine stopped."

# class Car(Vehicle):
#     def __init__(self, brand, model, num_doors):
#         super().__init__(brand, model)
#         self.num_doors = num_doors

#     def honk(self):
#         return f"{self.brand} {self.model} is honking!"

# Car1 = Car("Toyota", "Camry", 4)
# print(Car1.start_engine())  # Inherited method
# print(Car1.honk())  # Car's own method
# print(Car1.stop_engine())  # Inherited method


# How many types of inheritance are there in python?
# The types of inheritance in Python are:
# single inheritance, multiple inheritance, multilevel inheritance, hierarchical inheritance, and hybrid inheritance.
# Now We will see the example of multilevel inheritance in python, with easy and short code.
# class Parent1:
#     def method1(self):
#         return "This is method 1 from Parent1"

# class Parent2(Parent1):
#     def method2(self):
#         return "This is method 2 from Parent2"

# class Child(Parent2):
#     def method3(self):
#         return "This is method 3 from Child"

# C1 = Child()
# print(C1.method1())
# print(C1.method2())
# print(C1.method3())


# Function Definition
def calculate_accuracy(correct, total):
    accuracy = (correct / total) * 100
    return accuracy

# Function Call
result = calculate_accuracy(85, 100)
print(result)  # Output: 85.0