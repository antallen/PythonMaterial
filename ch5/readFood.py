# 引用 csv 類別
import csv

# 開啟 CSV 檔案
with open('food.csv', newline='') as csvfile:

    # 讀取 CSV 檔案內容,可指定分隔符號
    rows = csv.reader(csvfile, delimiter=',')

    # 以迴圈輸出每一列
    for row in rows:
        print(row)