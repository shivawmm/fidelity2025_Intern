# try:
#     print(10/0)
# except:
#     print("An error occurred")
# print("Hi")




# try:
#     x = int(input("Enter the number: "))
#     y = int(input("Enter the number: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("Error")
# except ValueError:
#     print("Value Error")




# # format of creating the exception in python
# class TooyoungException(Exception):
#     def __init__(self, msg):
#         self.msg = msg

# age = 10
# if age <= 18:
#     raise TooyoungException("You are too young")







# class TooyoungException(Exception):
#     def __init__(self, msg):
#         self.msg = msg
# class Employee:
#     def __init__(self, name, role, id):
#         self.name = name
#         self.role = role
#         self.id = id
#     def validate_id(self):
#         if not self.id.isdigit():
#             raise TooyoungException("Id must be numeric")
#         if len(self.id) != 4:
#             raise TooyoungException("Id must be 4 digit long")
#         else:
#             print("Welcome")
#     def __str__(self):
#         return f"Name: {self.name}, Role: {self.role}, ID: {self.id}"
# your_name = input("Enter employee name: ")
# role = input("Enter employee role: ")
# id = input("Enter employee ID: ")
# e = Employee(your_name, role, id)
# e.validate_id()
