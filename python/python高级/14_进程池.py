from multiprocessing import Pool
import os
import time

def worker(num):
    for i in range(5):
        print("===pid=%d==num=%d="%(os.getpid(),num))
        time.sleep(1)

pool = Pool(3)

for i in range(10):
    print("---%d---"%i)

    pool.apply_async(worker,(i,))

pool.close()
pool.join()
