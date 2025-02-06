# class P:
#     a = 10
#     def __init__(self):
#         self.b=20
#     def m1(self):
#         print("Parent instance method")
#     @classmethod
#     def m2(cls):
#         print("class method")
#     @staticmethod
#     def m3():
#         print("static method")
# class C(P):
#     pass
# c=C()
# c.m1()
# c.m2()
# c.m3() 



# class Person:
#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id

#     def getinfo(self):
#         return (self.name, self.age, self.id)
# class Employee(Person):
#     def __init__(self, name, age, id, sal):
#         self.salary = sal
#         super().__init__(name, age, id)

#     def employee_details(self):
#         # self.getinfo()
#         # print(self.salary)
#         print(super().getinfo(),self.salary)

# person = Person("Shivam Singh", 22, 785623)
# person.getinfo()
# employee = Employee("Shivam Singh", 22, 785623, 70000)
# employee.employee_details()
    







# # mro
# class A:
#     def method(self):
#         print("A's method")

# class B(A):
#     def method(self):
#         super().method()

# class C(A):
#     def method(self):
#         super().method()

# class D(B,C):
#     def method(self):
#         return super().method()

# d = D()
# d.method()







# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         msg = f'name is {self.name}, age is {self.age}'
#         return msg
#         # return ("Name is {0} and Age is {1}".format(self.name, self.age))
# s1 = Student("Steve", 40)
# print(s1)