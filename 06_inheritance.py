from calendar import c


class A:
    def Adata(self):
        print("Method of A")
    def getdata(self):
        print("in A")

class B:
    def Bdata(Self):
        print("Method of B")
    def getdata(self):
        print("in B")

class C(B,A):
    def Cdata(self):
        print("Method of C")

ob=C()
ob.getdata()