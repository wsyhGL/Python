class SendPower:

    def __sendMaging(self):
        print("——————正在发送——————")

    def sendMag(self , newNum):
        if newNum >100:
            self.__sendMaging()
        else:
            print("余额不足")

send = SendPower()
send.sendMag(102)
