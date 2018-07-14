temperature = 0
def set_t():
    global temperature
    temperature = 24

def print_t():
    print("当前的温度：%d"%temperature)

set_t()
print_t()

