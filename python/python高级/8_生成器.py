def creatNUm():
    a,b=0,1
    for i in range(5):
        yield b
        a,b = b,a+b

a = creatNUm()
b = next(a)
#b=a.__next__()#另一种方式
print (b)
