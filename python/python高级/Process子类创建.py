from multiprocessing import Process
import time

class NewProcess(Process):
    def run(self):
        while True:
            print("---1---")
            time.sleep(1)

p = NewProcess()
p.start()
while True:
    print("---main---")
    time.sleep(1)
