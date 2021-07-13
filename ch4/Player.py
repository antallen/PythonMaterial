class Player:
    # 初始化玩家，每人發 20000 遊戲幣以及出發位置為 0
    def __init__(self,money = 20000, po = 0):
        self.__money = money
        self.__po = po
        
    # 設定玩家名稱
    def setName(self,name):
        self.__name = name
        
    # 取得玩家名稱
    def getName(self):
        return self.__name
        
    # 修改玩家遊戲幣
    def setMoney(self,money):
        self.__money += money
        
    # 取得玩家遊戲幣
    def getMoney(self):
        return self.__money
        
    # 修改玩家位置
    def setPo(self,move):
        self.__po += move
        
    # 取得玩家位置
    def getPo(self):
        return self.__po