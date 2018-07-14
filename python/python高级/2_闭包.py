def test(number):
    print("-----1-----")

    def test_in(number2):
        print("----2-----")
        print(number+number2)
    print("------3-----")
    return test_in

resr = test(100)
resr(100)
