import pickle
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
dict1 = {'name': 'Alice', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}
with open('data.txt', 'wb') as f:
    pickle.dump(list1, f)
    pickle.dump(list2, f)
    pickle.dump(dict1, f)
    pickle.dump(dict2, f)