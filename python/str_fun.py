class Cat:
    #初始化对象
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    def __str__(self):
        return "%s的年龄是:%d"%(self.name,self.age)

    #方法

    def eat(self):
        print("猫在吃鱼")

    def drink(self):
        print("喝水")

    def intor(self):
        print("%s的年龄是%d"%(self.name,self.age))

#创建一个对象
tom = Cat("TOM",10)
lanmao = Cat("BlueCat",10)

print(tom)
print(lanmao)

