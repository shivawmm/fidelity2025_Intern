import csv
with open("data.csv","w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Name","Age","Gender"])
    w.writerow(["John","20","Male"])
    w.writerow(["Anna","25","Female"])
# It will mclose in its own


f = open("data.csv", "r")
r = csv.reader(f)
data = list(r)
print(data)