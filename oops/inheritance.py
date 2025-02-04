class P:
    a = 10
    def __init__(self):
        self.b=20
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("class method")
    @staticmethod
    def m3():
        print("static method")
class C(P):
    pass
c=C()
c.m1()
c.m2()
c.m3() 