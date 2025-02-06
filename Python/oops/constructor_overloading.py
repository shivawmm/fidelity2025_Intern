class Example:
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
    def __str__(self):
        return str(self.a)

e1 = Example()
e2 = Example(10)
print(e2)