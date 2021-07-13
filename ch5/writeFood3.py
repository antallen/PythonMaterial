# 引用 csv 類別
import csv

# 開啟輸出的 CSV 檔案
with open('food2.csv', 'w', newline='') as csvfile:
  # 定義欄位
  fieldnames = ['茶飲', '價錢']

  # 將 dictionary 寫入 CSV 檔
  writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

  # 寫入第一列的欄位名稱
  writer.writeheader()

  # 寫入資料
  writer.writerow({'茶飲': '綠茶', '價錢': 30})
  writer.writerow({'茶飲': '紅茶', '價錢': 35})