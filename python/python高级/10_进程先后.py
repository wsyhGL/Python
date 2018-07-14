import os
import time

ret = os.fork()

if ret == 0:
    print("---子进程---")
    time.sleep(5)
    print("---子进程完成---",end="")

else:
    print("---父进程---")
    time.sleep(3)
