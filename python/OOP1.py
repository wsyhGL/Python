class Cat:
    #属性

    #方法
    def eat(self):
        print("猫在吃鱼")

    def drink(self):
        print("喝水")

    def intor(self):
        print("%s的年龄是%d"%(self.name,self.age))

#创建一个对象
tom = Cat()

tom.eat()

tom.drink()

tom.name = "Tom"
tom.age = 10
tom.intor()

lanmao = Cat()
lanmao.name = "蓝猫"
lanmao.age = 10
lanmao.intor()


