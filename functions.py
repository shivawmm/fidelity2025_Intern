# def param_function(a,b):
#     return (a*b)
# print(param_function(10,5))







# def dsp(name, age):
#     print(name, age)
# dsp(name="Shivam", age=88)






# l = [10,20,40,80]
# def f1(l):
#     return sum(l), min(l), max(l)
# s1, min, max = f1(l)
# print(s1, min, max)







# # k-args function
# def f1(*a):
#     print(sum(a))
# f1(10)
# f1(10,20,30)








# def f1(**a):
#     print(a)
# f1(name="steve", age = 49)







# t1 = ()
# print(type(t1))






# def s1(a,b):
#     return (a+b)
# p = s1
# print(p(10,20))






# def f1():
#     def f2():
#         return("Hello")
#     return f2
# print(f1()())
    # return f2()
# print(f1())
# both can work






# # this is known as closure function
# def f1(a):
#     def f2():
#         print(a)
#     return f2()
# f1(10)







# data = 10
# # we don't have the access to use this variable inside out function until its global variable
# def f1():
#     global data
#     data = data +10
#     return data
# print(f1())











# l1 = [10,3,4,5,90]

# l2= iter(l1)
# print(next(l2))








# import sys
# l1 = [i for i in range(100000)]
# g = (i for i in range(100000))
# print(sys.getsizeof(l1))
# print(sys.getsizeof(g))





# def f1():
#     print("hello")
# def f2(a):
#     return a()
# f2(f1)






# input1 = eval(input("Enter first input: "))
# input2 = eval(input("Enter second input: "))
# def add(x,y):
#     return x+y
# def test(a):
#     global input1
#     global input2
#     return a(input1,input2)
# print(test(add))

























