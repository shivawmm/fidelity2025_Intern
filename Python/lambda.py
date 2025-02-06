# numbers = [1, 2, 3, 4, 5]

# # Use lambda function with map to square each number
# squared_numbers = list(map(lambda x: "even" if x % 2 == 0 else "odd", numbers))
# print(squared_numbers)

from collections import defaultdict
def dv():
    return "Key is not found"
d1 = defaultdict(dv)
d1['a'] = 10
d1['b'] = 20
print(d1['c'])
