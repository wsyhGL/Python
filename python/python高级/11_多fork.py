import os
import time

ret = os.fork()
if ret == 0:
    print("---process1---")

else:
    print("---process2---")
ret = os.fork()
if ret == 0:
    print("---process11---")

else:
    print("---process22---")
