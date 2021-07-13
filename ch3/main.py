##############################
# Project: 大富翁遊戲主程式   #
# Version: 0.1               #
# Date: 2021/07/07           #
# Author: Antallen           #
# Content: 使用 Player 物件
##############################

# 引用 random 類別中的 randrange() 函數
from random import randrange

# 引用 Player 物件
import Player

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

    # 開始進行遊戲
    while True:    
    ##### a.)
    ##### b.) 擲骰子
        newstep = randrange(1,6)
        print(players[i].getName() + "擲骰子：" + str(newstep) + " 點")
        print(players[i].getName() + "前進中...")
        # 設定玩家新的位置
        players[i].setPo(newstep)
    ##### c.)
    ##### e.)
        # 輪至下一位玩家
        if (i < players_num):
            i = i + 1
        else:
            i = i - players_num

        players_num = players_num - 1 # 測試 while 迴圈用
        print(players_num)
        
    ##### f.) 結束遊戲條件
        if (players_num <= 1):
            print("遊戲結束")
            break