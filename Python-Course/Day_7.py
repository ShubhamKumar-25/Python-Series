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




# Processing JSON-like API data using List of Dicts
students = [
    {"id": 101, "name": "Aman", "marks": 88},
    {"id": 102, "name": "Priya", "marks": 95}
]
print(students[1]["name"])
print(students)

raw_labels = ["cat", "dog", "cat", "bird", "dog"]
unique_labels = set(raw_labels) 
print(unique_labels)



# Standard loop
squares = []
for x in range(10):
    squares.append(x**2)

# List Comprehension
squares = [x**2 for x in range(10)]
print(squares)