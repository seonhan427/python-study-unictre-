class TV:
    def __init__(self, channel=5, volume=10, on=False):
        self.__channel = channel
        self.volume = volume
        self.on = on

    def show(self):
        print('channel:{},volume:{}, ON/OFF:{}'.format(self.__channel,self.volume,self.on))
    
    def setChannel(self, channelNum):
        if 1 < channelNum <99:
            self.__channel = channelNum
        else:
            print('체널 번호가 올바르지 않습니다. 기시입력해주세요')
    def getChannel(self):
        return self.__channel

myTv = TV(channel=15)
myTv.show()

myTv.setChannel(-9876543)
myTv.show()

myTv.setChannel(22)
myTv.show()
