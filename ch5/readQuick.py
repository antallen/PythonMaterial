# 讀取檔案內容
files = open("stores.txt","r", encoding='utf-8')

# 建立一個空的串列，準備接收檔案的每一行文字
stores = []

# 利用 readlines 將每一行文字，放入串列
stores = files.readlines()

print(stores)