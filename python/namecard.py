#打印提示
print("*"*50)
print("  名片管理系统 V1.10")
print("1.添加名片")
print("2.删除名片")
print("3.修改名片")
print("4.查询名片")
print("5.显示名片")
print("6.退出系统")

#存储名片
card_ifros = []
while True:
    #   获取用户的输入
    num = int(input("请输入操作序号:"))

    #3.根据用户的数据执行相应的操作
    if num == 1:
        newName = input("请输入新的姓名：")
        newQQ = input("请输入新的QQ：")
        newWeiXin = input("请输入新的微信：")
        newAddress = input("请输入新的地址：")
        
        newInfor = {}
        newInfor['name'] = newName
        newInfor['qq'] = newQQ
        newInfor['weixin'] = newWeiXin
        newInfor['address'] = newAddress

        #将字典，添加到列表中
        card_ifros.append(newInfor)
        print(card_ifros)
    elif num ==2:
        pass
    elif num ==3:
        pass
    elif num ==4:
        findInt = 0#默认为0没有找到
        findName = input("请输入要查询的姓名：")
        for temp in card_ifros:
            if findName == temp['name']:
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))
                findInt = 1;#找到
                break
        if findInt == 0:
            print("没有此人信息")
    elif num ==5:
        print("姓名\tQQ\t微信\t地址")
        for temp in card_ifros:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))
    elif num ==6:
        break
    else:
        print("输入有误，请重新输入")

    print("")
