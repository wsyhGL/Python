class Test(object):
    def __init__(self):
        self.__number = 100

    @property
    def number(self):
        return self.__number

    @property.setter
    def number(self,newNumber):
        self.__number = newNumber



t = Test()
t.number = 200
print(t.number)
