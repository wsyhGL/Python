from multiprocession import Pool
import os
import Manager

def copyFileTask(name,oldFolderName,newFolderName,queue):
    #完成文件夹的拷贝
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name,"w")
    conent = fr.read();
    fw.write()

    fr.close()
    fw.close()
    queue.put()

def main():
    oldFileName = input("请输入文件夹的名字：")

    #创建一个文件夹
    newFileName = oldFileName+".复件"
    os.mkdir(newFileName)
    #获取old文件夹中的文件
    fileName = os.listdir(oldFileName)

    pool = Pool(5)
    queue = Manager().Queue()

    for name in fileName:
        pool.apply_async(copyFileTask,args=(name,oldFileName,newFileName,queue))
    num = 0
    allNum = len(fileName)
    while num<allNum:
        queue.get()
        num+=1
        copyReta = num/allNum
        print("\rcopy的进度：%.2f%%"%(copyReta*100),end=" ")

    print("\n")

if __name__ = "__main__":
    main()
