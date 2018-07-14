from multiprocessing import Process
import os

#子进程要执行的程序
def run_proc(name):
    print("子进程运行中，name=%s,pid=%d..."%(name,os.getpid()))

if __name__=="__main__":
    print("父进程 %d"%(os.getpid()))
    p = Process(target=run_proc,args=("test",))
    print("子进程执行")
    p.start()
    p.join()
    print("子进程执行结束")
