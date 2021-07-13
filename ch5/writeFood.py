# 引用 csv 類別
import csv

# 開啟輸出的 CSV 檔案
with open('food2.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile, delimiter=',')

    # 寫入一列資料
    writer.writerow(['茶飲', '價錢'])

    # 寫入另外幾列資料
    writer.writerow(['綠茶', 30])
    writer.writerow(['紅茶', 35])