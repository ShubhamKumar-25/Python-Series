# info = {
#     "Name": "Rohan Gupta",
#     "age": 22,
#     "is_student": True,
#     "city": "Motihari",
#     "Salary": 30000
# }

# print(info)

info = {
    "Name": "Rohan Gupta",
    "Subjects": ["JAVA", "C++", "PYTHON", "JAVASCRIPT"],
    "Topic": ("Dist", "Set"),
    "Marks": 89.0,
    "is_Student": True,
    "City": "Motihari",
    "age": {22} # that is exceptional
}
# print(info)
# print(type(info))
print(info["Name"])
print(info["Subjects"])
print(info["Topic"])
print(info["age"])