#实现文件的复制
oldFileName = input("输入要复制的文件名")

oldFile = open(oldFileName,"r")

position = oldFileName.rfind(".")
newFileName = oldFileName[:position]+"[附件]"+oldFileName[position:]
newFile = open(newFileName,"w")

while True:
    content = oldFile.read(1024)
    if len(content)==0:
        break

    newFile.write(content)

oldFile.close()
newFile.close()

