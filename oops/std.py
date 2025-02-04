# class Student:
#     """This is student class"""
#     def __init__(self):
#         self.name = "Steve"
#         self.age = 40
#     def dsp(self):
#         print(self.name, self.age)
# s=Student()
# s.dsp()



# class Student:
#     a=10
#     def dsp(self):
#         print(self.a)
#     @classmethod
#     def m1(cls):
#         print(cls.a)
# s = Student()
# s.m1()



class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append("Deposited: " + str(amount))
        return self.balance

        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append("Withdrawn: " + str(amount))
        return self.balance
s=Customer("Shivam", 1000)
print(s.deposit(1000))
print(s.withdraw(500))