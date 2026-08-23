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


# collection = {1,2,3,4}
# print(collection)
# print(type(collection))

# data = {2, 4, 4, 2, "Hello", "JAVA", "java", "World", "WOrld", "Hello", 1, 2}
# print(data)
# print(len(data))


# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.add(5)
# collection.add(3)
# collection.add(5)
# collection.remove(5)
# collection.add((12,3,4,5,6))
# collection.add("Rohan Gupta")
# # collection.add([1,2,3,4,5,6]) # list be not allowed in set 
# # print(collection)
# # print(len(collection))
# # collection.clear()
# # print(collection.clear())
# print(collection)

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))


# marks = {}
# x = int(input("Enter Phy: "))
# marks.update({"Phy :": x})

# x = int(input("Enter Che: "))
# marks.update({"Che :": x})

# x = int(input("Enter math: "))
# marks.update({"math :": x})

# print(marks)


# values = {
#     ("int", 9),
#     ("float", 9.0)
# }
# print(values)

nums = [1,2,3,5,6,7,8,9]
for val in nums:
    print(val)