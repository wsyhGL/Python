class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self, carType):
        return self.factory.selectType(carType)

class Factory(object):
    def selectType(self,carType):
        if carType=="s":
            return Sun()
        elif carType=="M":
            return M()

class Car(object):
    def move(self):
        print("move")

class Sun(Car):
    pass
class M(Car):
    pass
car = CarStore()
car1 = car.order("s")
car1.move()
