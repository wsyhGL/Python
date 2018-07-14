class Person(object):
    """英雄类"""
    def __init__(self,name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None#保存枪的引用
        self.hp = 100
    
    def anzhuang_zd(self,dan_jia_temp, zi_dan_temp):
        """将子弹安装到弹夹 """
        dan_jia_temp.save_zd(zi_dan_temp)

    def anzhuang_danjia(self,gun_temp,dan_jia_temp):
        """安装弹夹"""
        gun_temp.save_danjia(dan_jia_temp)

    def take(self,gun_temp):
        self.gun = gun_temp
    
    def __str__(self):
        if(self.gun):
            return "英雄名字：%s,血量：%d，武器信息：%s"%(self.name,self.hp,self.gun)
        else:
            return "英雄名字：%s，血量：%d,没有武器"%(self.name,self.hp)

    def attack(self, diren):
            #枪开火
            self.gun.fire(diren)

    def hit(self,num):
            self.hp -= num


class Gun(object):
    def __init__(self,name):
        """枪类"""
        super(Gun,self).__init__()
        self.name = name
        self.danjia = None#记录弹夹对象引用

    def save_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp

    def __str__(self):
        if self.danjia:
            return "枪的信息：%s,%s"%(self.name,self.danjia)
        else:
            return "枪的信息：%s,没有弹夹"%(self.name)

    def fire(self,diren):
        #弹出一个子弹
        zidan1 = self.danjia.pop_zidan();
        if zidan1:
            zidan1.jizhong(diren)
        else:
            print("没有子弹")

class DanJi(object):
    def __init__(self,max_num):
        super(DanJi,self).__init__()
        self.max_num = max_num
        self.zidan_list = []#保存子弹因用

    def save_zd(self,zi_dan_temp):
        self.zidan_list.append(zi_dan_temp)

    def __str__(self):
        return "弹夹的信息：%d/%d"%(len(self.zidan_list),self.max_num)

    def pop_zidan(self):
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None


class ZIDAN(object):
    """子弹类"""
    def __init__(self ,num):
        super(ZIDAN,self).__init__()
        self.num = num

    def jizhong(self,diren):
        diren.hit(self.num)

def main():
    '''
    控制程序的流程
    '''
    pass
#1.创建英雄
wang = Person("Wang")
#2.创建枪
MA4 = Gun("MA4")
#3.创建弹夹
danjia = DanJi(30)
for i in range(15): 
    #4.创建子弹 
    zd = ZIDAN(10)
    #6.安装子弹
    wang.anzhuang_zd(danjia,zd)
#7.安装弹夹
wang.anzhuang_danjia(MA4,danjia)
#8.拿枪
wang.take(MA4)
#创建敌人
son = Person("son")
#9.打敌人
wang.attack(son)

#test:
print(danjia)
print(MA4)
#测试英雄
print(son)
print(wang)
if __name__ =="__main__":
    main()

