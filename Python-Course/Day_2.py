

# variable in python
# name = "Shubham"
# age = 23
# role = "MERN Developer"

# print(name)
# print(age)
# print(role)

# name = "Rohan"
# message = "Hello " + name
# print(message)


# name = "Shubham"
# age = 23
# print(f"My name is {name} and I am {age} years old.")

# variable ki value change karna 
# city = "Motihari"
# print(city)
# city = "Punjab"
# print(city)


# print("----------------------------------------------------------")

# userName = "Rohit Gupta"
# password = 1234
# print(f"UserName: {userName}" )
# print(f"password: {password}")



# String In Python
# str = "Hey Everryone Rohan Gupta this side.\nWhat about you?"
# print(str)

# str = "Rohan Gupta"
# print(len(str))
# str1 = "Collage"
# print(len(str1))

# indexing and length
# str = "Rohan Gupta"
# print(len(str))
# print(str[4])
# print(str[6])


# Slicing is python
# str = "Apple"
# print(str[1 : 4])
# print(str[0 : 6])
# print(str[4 : 9])

# str = "Rohan_Gupta"
# print(str[3 : 8])
# print(str[: 6]) # [0 : 6] python assume that it start from zero(0)
# print(str[2: ]) # [2 : len(str)] python assume that it is end with length of the string


# Ends with string
# print(str.endswith('ege'))
# print(str.startswith('am'))
# print(str.startswith('I'))


# str = "apple"
# str1 = "Lion"
# print(str1)
# print(str1.lower())
# print(str.capitalize())

# str = "I am studying python from apnacollege"
# print(str.replace("o", "z"))
# print(str.replace("python", "javascript"))

# str = "kya hal hai bhai sab"
# print(str.find("hai"))


# str = "6352676727716366477474778828310"
# print(str.count("7"))
# print(str.count("4"))
# print(str.count("6"))
# print(str.count("10"))
# print(str.count("77"))


# str = input("Enter your name: ")
# print(len(str))

# doller = "kya hal hai $ dosto $ aur sab thik hai$, sab kusal mangal$ hai na $"
# print(doller.count("$"))

# age = 8
# if(age >= 18):
#     print("can vote and can apply to licence")
# elif(age <= 10):
#     print("not eligibal")


# light = "Black"
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("Ready")
# elif(light == "green"):
#     print("go")
# else:
#     print("Light is broken")

# num = (int(input("Enter your number: ")))
# if(num % 2 == 0):
#     print("Even")
# else:
#     print("odd")

# print("-------------------------------------")
# num2 = (int(input("Enter your number: ")))
# if(num2 % 7 == 0):
#     print("Yes")
# else:
#     print("No")

# print("--------------------------------------")
# a = 10
# b = 20
# c = 90
# if(a>=b and b>=c):
#     print(a)
# elif(b>=c):
#     print(b)
# else:
#     print(c)


# moves = []
# mov1 = input("Enter your 1st move :")
# mov2 = input("Enter your 2nd move :")
# mov3 = input("Enter your 3th move :")
# moves.append(mov1)
# moves.append(mov2)
# moves.append(mov3)
# print(moves)

# lts = list(map(int, input("Enter your number: ").split()))
# copy_lts = lts.copy()
# copy_lts.reverse()
# if(lts == copy_lts):
#     print("it is a palindrome")
# else:
#     print("Not palindrome")


# lts = input("Enter your string: ").split()
# copy_lts = lts.copy()
# copy_lts.reverse()
# if(lts == copy_lts):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# grad = ("A", "B", "A", "A", "C")
# print(grad.count("C"))

# lts = ["A", "B", "A", "A", "C", "K", "O"]
# lts.sort()
# print(lts)

num = list(map(int, input("Enter your number :").split()))
num.sort()
print(num)