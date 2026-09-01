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

class Account:
    def __init__(self, account_number, account_password):
        self.account_number = account_number
        self.__account_password = account_password  # Private attribute
        self.__account_balance = 0.0  # Private attribute

    def reset_pass(self, new_password):
        self.__account_password = new_password
A1 = Account("123456789", "securepassword")
print(A1.account_number)  # This will work
# print(A1.__account_password)  # This will raise an AttributeError since '__account_password' is private
A1.reset_pass("newsecurepassword")  # This will work