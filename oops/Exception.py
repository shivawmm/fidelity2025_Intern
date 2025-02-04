# try:
#     print(10/0)
# except:
#     print("An error occurred")
# print("Hi")




try:
    x = int(input("Enter the number: "))
    y = int(input("Enter the number: "))
    print(x/y)
except ZeroDivisionError:
    print("Error")
except ValueError:
    print("Value Error")