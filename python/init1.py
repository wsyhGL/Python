class Cat:
    #初始化对象
    def __init__(self,newName,newAge):
        self.name = newName
        self.age = newAge

    #方法

    def eat(self):
        print("猫在吃鱼")

    def drink(self):
        print("喝水")

    def intor(self):
        print("%s的年龄是%d"%(self.name,self.age))

#创建一个对象
tom = Cat("TOM",10)
tom.eat()
tom.drink()

tom.intor()

lanmao = Cat("BlueCat",10)
lanmao.intor()


