class Test(object):
    def __init__(self):
        self.__number = 100

    def getNumber(self):
        return self.__number

    def setNumber(self,newNumber):
        self.__number = newNumber

    num = property(getNumber,setNumber)


t = Test()
t.num = 200
print(t.num)
