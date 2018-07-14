class Base(object):
    def test(self):
        print("====Base====")

class A(Base):
    def test(self):
        print("====A====")

class B(Base):
    def test(self):
        print("====B====")

class C(A,B):#多继承
    pass

c = C()
print(C.__mro__)#c的
