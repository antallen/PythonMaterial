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
print(players_name)
print(moneys)

# 開始進行遊戲
while True:
##### a.)
##### b.)
##### c.)
##### e.)
    players_num = players_num - 1 # 測試 while 迴圈用
    print(players_num)
##### f.) 結束遊戲條件
    if (players_num <= 1):
        print("遊戲結束")
        break