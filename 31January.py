# i = 0
# even = 0
# odd = 0
# for i in range(i, 101):
#     if i%2 == 0:
#         even += 1
#     else:
#         odd += 110
# print (odd, even)


# count = 0
# for i in range(100, 10000):
#     if i % 5 == 0 and i%7 == 0:
#         count += 1
# print (count)


# count = eval(input("Enter the number: "))
# for i in range(2, count):
#     if count%i == 0:
#         print(i)
# print(count)


# start = eval(input("Enter the startig number: "))
# end = eval(input("Enter the ending number for range: "))
# count = 0
# for num in range(start, end + 1):
#     if num < 2:
#         continue
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)
# print("Count of prime numbers in the range is ", count)


# for i in range(10):
#     if i % 10 == 0:
#         print(i) 
#         continue


# num = int(input("Enter the number "))
# count = 0
# while(num>0):
#     num = num//10
#     count += 1
# print(count)


# for i in range(3):
#     name = str(input("Enter your name: "))
#     if(name == "Shivam"):
#         print("Welcome")
#     elif(i == 2):
#         print("Locked")


# # Lists
# l =[1, "hello", 67.7, False]
# # print(type(l))
# l.reverse()
# print(l)
# # print(l[-1])


# l1 = [2,3,4,5]
# l2=l1
# l2.append(200)
# print(l1)  # [2, 3, 4, 5, 200
# print(l2)
# # this is known as shallow copy


# l1 = [2,3,4,5]
# l2=l1.copy()
# l2.append(200)
# print(l1)  # [2, 3, 4, 5, 200]
# print(l2)
# # this is known as deep copy


# s1 =[45,56,89,70]
# s2 =[47,50,43,60]
# s3=[23,56,77,50]
# s=[s1,s2,s3]
# for i in s:
#     for j in i:
#         if j < 35:
#             print(j)
# print(sum(s1))


# l1 = [i for i in range(200) if i%2!=0]
# print(l1)

# l2 = ['Bob', 23,68,56,44,45]
# name, age, *marks, gender = l2
# print(name, age, marks)
# print(marks)
# print(name, age, marks, gender)
# # this is known as packing and unpacking


# l1 = [1,2,4,5,7,8,5,7,9]
# l1.remove(5)
# print(2 not in l1) # this is membership operator
# print(l1)  # [1, 2, 4, 7, 8

# l1 = [1,2,4,5,7,8,5,7,9]
# l2 = []
# for i in l1:
#     if i not in l2:
#         l2.append(i)
# l1 = l2
# print(l1)


# dictionary
# d1 = {'name':'Bob', 'age':23, 'marks':90}
# d2 = {'name':'Bob', 'age':23, 'name':'Joe'}
# print(d2)
# print(d1['age'], d1['name'])
# d3 = {'name':'Bob', 'age':23, 'name':'Joe'}
# for n in d3.values():
#     print(n)
# for n,v in d3.items():
#     # print(n,v)
#     print(n,v, sep=' = ') 
# d4 = {'name':'Bob', 'age':23, 'name':'Joe'}



# keys=['name', 'age', 'place']
# val=['Bob', 44, 'Bangalore']
# d1 = {key: value for key, value in [(keys[i], val[i]) for i in range(len(keys))]}
# d2 = zip(keys, val)
# print(dict(d2))
# d3 = {i: i*2 for i in range(11)}
# print(d3)


# d1 = {'name': 'Rahul', 'skill': ['C', 'C++', 'Java']}
# d2 = {'name': 'nyaare', 'skill': ['C', 'Go', 'Python']}
# d3 = {'name': 'pyaare', 'skill': ['C', 'Go', 'Java']}
# skill_needed = 'Python'
# list = [d1, d2, d3]
# python_dict = [d for d in list if skill_needed in d['skill']]
# print(python_dict)


# Set 


