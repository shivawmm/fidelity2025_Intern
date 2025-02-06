import os
for dirpath, dir, file in os.walk("."):
    for i in file:
        if i.endswith(".py"):
            print(i)