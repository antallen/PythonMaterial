# 引用 random 類別中的 randrange() 函數
from random import randrange

# 要求玩家要輸入遊戲人數
players_num = eval(input("請輸入玩家人數："))

# 設定一開始的遊戲幣
moneys = []

# 設定玩家名單
players_name = []

# 按照遊戲人數，輸入玩家名稱，以及增加遊戲幣數量
for i in range(players_num):
    # 要求玩家輸入玩家名稱
    players = input("請輸入玩家名稱:")
    # 將玩家名稱列入玩家資料陣列
    players_name.append(players) 
    # 增加遊戲幣數量
    moneys.append(20000) 

# 輸出資料
print(players_name[0])
print(moneys[0])

# 設定玩家順序值
i = 0

# 開始進行遊戲
while True:    
##### a.)
##### b.) 擲骰子
    newstep = randrange(1,6)
    print(players_name[i] + "擲骰子：" + str(newstep) + " 點")
    print(players_name[i] + "前進中...")
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