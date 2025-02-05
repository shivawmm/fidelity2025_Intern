import pickle
with open('data.txt', 'rb') as f:
    data = []
    while True:
        try:
            item = pickle.load(f)
            data.append(item)
        except EOFError:
            break
dictionaries = [item for item in data if isinstance(item, dict)]
for i, dictionary in enumerate(dictionaries):
    print(f"Dictionary {i+1}: {dictionary}")