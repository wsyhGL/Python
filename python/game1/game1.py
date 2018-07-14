class Person(object):
    """英雄类"""
    def __int__(self,name):
        super(Person,self).__init__()
        self.name = name

    def anzhuang_zd(self,dan_jia_temp, zi_dan_temp):
        """将子弹安装到弹夹 """
        dan_jia_temp.save_zd(zi_dan_temp)

    def anzhaung_danjia(self,gun_temp,dan_jia_temp):
        """安装弹夹"""
        gun_temp.save_danjia(dan_jia_temp)

class Gun(object):
    def __init__(self,name):
        """枪类"""
        super(Gun,self).__init_()
        self.name = name
        self.danjia = None#记录弹夹对象引用

    def save_danjia(self,dan_jia_temp):
        self.danjia = dan_jia_temp

class DanJi(object):
    def __init__(self,max_num):
        super(DanJi,self).__init__()
        self.max_num = max_num
        self.zidan_list = []#保存子弹因用

    def save_zd(self.zi_dan_temp):
        self.ziidan_list,append(zi_dan_temp)
class ZIDAN(object):
    """子弹类"""
    def __init__(self ,num):
        super(ZIDAN,self).__init__()
        self.name = name

    

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
#4.创建子弹
zd = ZIDAN(10)
#5.创建敌人
#6.安装子弹
wang.anzhuang_zd(danjia,zd)
#7.安装弹夹
wang.anzhuang_danjia(MA4,danjia)
#8.拿枪
#9.打敌人
if __name__ =="__main__":
    main()

