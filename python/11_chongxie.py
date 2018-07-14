class Animal:
    def eat(self):
        print("-----eat-----")

    def bark(self):
        print("======bark====")

class dog(Animal):
    def bark(self):
        print("Bigeat")
       #第一种调用
       #Animal.bark(self)
       #第二种
        super().bark()

su = dog()
su.bark()
