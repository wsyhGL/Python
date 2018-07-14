class Tool(object):
    #类属性
    num = 0

    def __init__(self, newName):
        #实例属性
        self.name = newName
        #对类属性操作
        Tool.num += 1

tool = Tool("A")
tool22 = Tool("B")
print(Tool.num)
