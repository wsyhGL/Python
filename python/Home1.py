class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain = []

    def __str__(self):
        ms = "房子的总面积：%d,可用面积：%d,户型：%s,地址是%s"%(self.area,self.left_area,self.info,self.addr)
        ms +="房子里的物品有%s"%(str(self.contain))
        return ms

    def add_item(self,item):
        self.left_area -= item.area
        self.contain.append(item.name)

class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area

fangzi = Home(129,"别墅","北京市")

bed = Bed("床",6)

fangzi.add_item(bed)

print(fangzi)

