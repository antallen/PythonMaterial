# 新增一家店名，店名後方，要加上"\n"
newstore = "\n北極熊火鍋店"

# 開啟檔案，設定成附加寫入模式
new_files = open("stores.txt","a", encoding='utf-8')

# 將串列寫入檔案中
new_files.writelines(newstore)

# 關閉檔案
new_files.close()