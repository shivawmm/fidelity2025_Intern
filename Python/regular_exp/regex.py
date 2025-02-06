import re
str = "steve3434 joe555"
l = re.findall("[0-9]*", str)
print(l)