#eval()函数的使用
def test(a,b,func):
    result = func(a,b)
    return result

func_new = input("请输入一个匿名函数：")

func_new = eval(func_new)

mun = test(11,22,func_new)
print(mun)

