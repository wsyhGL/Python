class SweetP:
    def __init__(self):
        self.cookedString = "生"
        self.cookedLevel = 0
        self.condiments = []

    def __str__(self):
        return "地瓜状态：%s(%d)%s"%(self.cookedString,self.cookedLevel,str(self.condiments))

    def cook(self,cookTime):
        self.cookedLevel += cookTime
        if self.cookedLevel >=0 and self.cookedLevel <=3:
            self.cookedString = "生"
        elif self.cookedLevel >=3 and self.cookedLevel <=5:
            self.cookedString = "半熟"
        elif self.cookedLevel >=5 and self.cookedLevel <=8:
            self.cookedString = "熟"
        elif self.cookedLevel >=8:
            self.cookedString = "焦"

    def addCondiments(self,item):
        self.condiments.append(item)
di_gua = SweetP()

di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.addCondiments("盐")
print(di_gua)

