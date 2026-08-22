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
# print(info["Name"]) This approach is very wrong. ye yeha to chal ja raha hai but bade bade program karte time isse nahi likhte hai
# print(info.get("Name")) ye ek best ways hai single val print karna ka. upper wala wrong ways hai
# print(info)
# print(type(info))
# print(info["Name"])
# print(info["Subjects"])
# print(info["Topic"])
# print(info["age"])

info1 = {
    "Name": "Rohan Gupta",
    "Marks": {
        "Math": 65,
        "Phy": 65,
        "Che": 60
    },
    "address": {
        "Country": "India",
        "State": "Bihar",
        "District": "Motihari",
        "Village": "Nawada",
        "Pin_code": 845417
    },
    "is_student": True
}

# print(info1["Marks"])
# print(info1["address"])
# print(info1.keys())
# print(info1.values())
# print(info1.items())
# print(info1["Name"])  This approach is very wrong. ye yeha to chal ja raha hai but bade bade program karte time isse nahi likhte hai
# print(info1.get("Name")) ye ek best ways hai single val print karna ka. upper wala wrong ways hai
# print(info1.get("Marks")) ye bhi ek best ways hai single val print karna ka. upper wala wrong ways hai 

# info1.update({"Age": 22})
# print(info1)
# print(info1.get("Age"))
# print(info1.values())
# print(info1.items())