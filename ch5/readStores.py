# 讀取檔案內容
files = open("stores.txt","r", encoding='utf-8')

# 建立一個空的串列，準備接收檔案的每一行文字
stores = []

# 利用迴圈將每一行文字，放入串列
for i in files:
	stores.append(i)
   
print(stores)
print("第五家店：",stores[4])

# 關閉檔案
files.close()