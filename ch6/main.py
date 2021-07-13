##############################
# Project: 大富翁遊戲主程式   #
# Version: 0.1               #
# Date: 2021/07/09           #
# Author: Antallen           #
# Content: 使用 Player 物件
##############################

# 引用 random 類別中的 randrange() 函數
from random import randrange

# 引用 Player 物件
import Player

# 引用 Chance 物件
import Chance

# 引用 Stores 物件
import Stores

# 引用 playMap 物件
import playMap

# 常用函式、參數設定區域
## 遊戲方格總數
areas = 24

## 處理玩家是否有經過「開始」
def playerPo(steps):
    if (steps >= areas):
        return (steps % areas)
    else:
        return steps

# 程式流程開始
# 使用 if __name__
if __name__ == "__main__":

    # 要求玩家要輸入遊戲人數
    players_num = eval(input("請輸入玩家人數："))

    # 建立玩家物件
    players = []

    # 按照遊戲人數，使用 Player 類別
    # 逐次產生玩家名稱、玩家代號、玩家初始遊戲幣、玩家初始位置等物件內容
    for i in range(players_num):
        players.append(Player.Player())
        # 要求玩家輸入玩家名稱
        players[i].setName(input("請輸入玩家名稱:"))
        
    # 輸出資料
    
    for i in range(players_num):
        print(players[i].getName())
        print(players[i].getPo())
        print(players[i].getMoney())
        
    # 設定玩家順序值
    
    i = 0
    myMap = playMap.playMap()
    players_po = ['0','0','0','0']
    # 開始進行遊戲
    while True:    
    ##### a.) 印出地圖
        myMap.printMap(players_po)
    ##### b.) 擲骰子
        input("按下 Enter 進行遊戲.....")
        newstep = randrange(1,6)
        print(players[i].getName() + "擲骰子：" + str(newstep) + " 點")
        print(players[i].getName() + "前進中...")
        # 設定玩家新的位置
        players[i].setPo(newstep)
        
    ##### c.) 移動到骰子點數的框格
        newpo = players[i].getPo() 
        #　I. 可能經過起點
        if newpo >= areas:
            newpo = playerPo(newpo)
            if newpo == 0:
                print("玩家回到「開始」位置：", newpo)
            elif newpo < (areas/4):
                print("玩家越過「開始」位置：", newpo)
        players_po[i] = str(newpo)
        myMap.printMap(players_po)
        print("玩家在新位置：",newpo)
        #  II. 可能落在邊角框格
        if (newpo  == 6):
            print("玩家休息一天")
        elif (newpo  == 18):
            print("玩家再玩一次")

        #  III. 可能是在機會與命運框格
        ## 機會的地圖編號是 3,15 兩個號碼
        elif ((newpo == 3) or (newpo == 15)):
            myChance = Chance.Chance()
            chances = myChance.choice()    
            print("玩家中機會：",chances[0])

        #  IV. 可能是在地產框格
        else:
            playerStore = Stores.Stores()
            store = playerStore.getStoreData(str(newpo))
            ## 判斷是否有人己取得該地產所有權了
            if store[2] == '-1':
                print("該地產無人所有！")
            else:
                print("該地產為：" + str(players[int(store[2])].getName()) + "所有")
           
    ##### e.)
        # 輪至下一位玩家
        i = i + 1
        if (i >= players_num):
            i = i - players_num
        
    ##### f.) 結束遊戲條件
        ends = input("是否結束遊戲？Ｙ：是　Ｎ：繼續")
        if ((ends == "Y") or (ends == "y")):
            break
