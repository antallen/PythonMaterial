# 引用 csv 類別
import csv

# 二維表格
table = [
    ['茶飲', '價錢'],
    ['綠茶', 30],
    ['紅茶', 35]
]

with open('food2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 寫入二維表格
    writer.writerows(table)