import types
class Person:
    def __init__(self,name,number):
        self.name=name;
        self.number = number

def eat(self):
    print("____%s"%self.name)


p1 = Person("GUU",19)
p1.eat=types.MethodType(eat,p1)
p1.eat()
