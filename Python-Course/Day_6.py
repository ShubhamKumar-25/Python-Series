# class Student1:
#     name = "Rohan Gupta"
# s1 = Student1()
# print(s1.name)


# class Car:
#     name = "BMW"
#     color = "Black"
#     model = "i1220"
# car1 = Car()
# print(car1.name)
# print(car1.color)



# # Parent Class
# class Animal:
#     def eat(self):
#         print("Eating food...")

# # Child Class (Animal ko inherit kar rahi hai)
# class Dog(Animal):
#     def bark(self):
#         print("Bhow Bhow!")

# my_dog = Dog()
# my_dog.eat()   # Parent ka feature use kiya
# my_dog.bark()  # Apna feature use kiya




class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding a new Element in database...")


    def welcome(self):
        print("Welcome student, ", self.name)

s1 = Student("Rahul", 89)
print(s1.name, s1.marks)

s2 = Student("Rohan", 90)
print(s2.name, s2.marks)
s2.welcome()