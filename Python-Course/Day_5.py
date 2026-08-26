
# # File input and output in python
# file = open("Student_records.txt", 'w')

# # Data write karna
# file.write("Name: Shubham\n")
# file.write("Course: B.Tech IT\n")
# file.write("Status: Active\n")
# file.write("Marks: 89\n")
# file.write("City: Motihari\n")
# file.close()
# print("File successfully created and data written!")


# with open("Student_records.txt", 'a') as file:
#     file.write("I am fullstack software develpoer \n")
# print("New Data append sucessfully")


# with open("Student_records.txt", "r") as file:
#     content = file.read()
#     print("-----Read file--------")
#     print(content)






# from datetime import datetime

# def log_activity(username, action):
#     # Current date and time fetch karna
#     current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
#     # Formatted log entry
#     log_entry = f"[{current_time}] USER: {username} | ACTION: {action}\n"
    
#     # Append mode 'a' use karenge taki purana log save rahe
#     with open("app_log.txt", "a") as log_file:
#         log_file.write(log_entry)

# # Log test cases
# log_activity("Shubham", "Logged In")
# log_activity("Shubham", "Executed Python Script")
# log_activity("Shubham", "Logged Out")

# # Ab logs check karte hain
# with open("app_log.txt", "r") as log_file:
#     print("\n--- Recent Logs ---")
#     print(log_file.read())


# 1. Function Defining (Banaye hain)
def greet():
    print("Hello! Welcome to Python Functions Series.")

# 2. Function Calling (Chala rahe hain)
greet()
greet()  # Reusability: jitni baar chaho call karo