# 將檔案內容讀出至串列
files = open("stores.txt","r", encoding='utf-8')
stores = []
for i in files:
    stores.append(i)
files.close()

# 最後一筆資料要處理換行的問題
stores[-1] = str(stores[-1] + "\n")

# 新增一家店名，店名後方，要加上"\n"
newstore = "北極熊火鍋店\n"

# 將新店家名稱加入 stores 串列
stores.append(newstore)

# 開啟檔案，設定成可寫入模式
new_files = open("stores.txt","w", encoding='utf-8')

# 將串列寫入檔案中
new_files.writelines(stores)

# 關閉檔案
new_files.close()