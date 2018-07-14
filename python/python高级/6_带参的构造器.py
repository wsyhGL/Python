def func_arg(per):
    def func(function):
        print("---func-1--")
        def func_in(*args):
            print("---func_in-1-per=%s-"%per)
            rest = function(*args)
            print("---func_in-2--")
            return rest

        print("---func-2--")
        return func_in
    return func

@func_arg("GUU")
def test(a,b,c):
    print("----test-a=%d,b=%d,c=%d"%(a,b,c))

test(11,22,33)
