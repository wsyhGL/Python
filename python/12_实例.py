class Game(object):

    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = "LXD"

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100

    #静态方法
    @staticmethod
    def print_menu():
        print("+++Play Game+++")


game = Game();
#Game.add_num()#可以通过类名调用类方法
game.add_num()#还可以通过对象调用
print(Game.num)

#Game.print_menu()
game.print_menu()
