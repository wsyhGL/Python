import os

folderName = input("请输入要重命名的文件：")

fileNames = os.listdir(folderName)

#os.chdir(folderName)

for name in fileNames:
    oldName = folderName+"/"+name
    newName = folderName+"/"+"[京东出品]"+name
    os.rename(oldName,newName)
