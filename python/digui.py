def test(num):
    if num>1:
        return num*test(num-1)
    else:
        return num

result = test(4)
print(result)

