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




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding a new Element in database...")


#     def welcome(self):
#         print("Welcome student, ", self.name)

# s1 = Student("Rahul", 89)
# print(s1.name, s1.marks)

# s2 = Student("Rohan", 90)
# print(s2.name, s2.marks)
# s2.welcome()


# class Student:
#     def __init__(self, sub1, sub2, sub3):
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
#         print("Printing marks...")

#     def average(self):
#         print((self.sub1 + self.sub2 + self.sub3) / 3)

# s1 = Student(87, 67, 89)
# s1.average()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.cluch = False

#     def Start(self):
#         self.cluch = True
#         self.acc = True
#         print("Car is Started....")

# c1 = Car()
# c1.Start()



class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs", amount, "was debiated.")
        print("Your total balance is", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs", amount, " is created in your account")
        print("Your total balance is", self.get_balance())

    def get_balance(self):
        return self.balance

A1 = Account(6000, 1122)
A1.debit(1000)
A1.credit(5000)