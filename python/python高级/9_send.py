def test():
    i=0
    while i<6:
        temp = yield i
        print(temp)
        i+=1

t = test()
t.__next__()
p = t.send("lxd")
print(p)

