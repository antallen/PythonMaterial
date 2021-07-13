import Stores

class playMap:

    def printMap(self):
        mapEmpty = "　"
        mapStoreName = "　　　　"
        mapStoreOwner = "　"
        mapStoreWall = "｜"
        mapStoreDev = "－"
        myStores = Stores.Stores()
        
        # 列出地圖十三大行
        for i in range(1,14):
            # 第二大行與第十二大行
            if ((i == 2) or (i == 12)):
                print(48*mapStoreDev)
            # 其他偶數行    
            elif ((i % 2) == 0):
                print(7*mapStoreDev, end = '')
                print(34*mapEmpty, end = '')
                print(7*mapStoreDev)
            # 第一與第十三大行均列出全部的地產
            elif ((i == 1) or (i == 13)):
                for k in range(1,4):
                    for j in range(0,7):
                        if i == 1:
                            print(mapEmpty + self.getStoreName(myStores.getStoreData(str(j))[1]) + mapStoreOwner, end = '')
                        elif i == 13:
                            print(mapEmpty + self.getStoreName(myStores.getStoreData(str(18-j))[1]) + mapStoreOwner, end = '')
                        print(mapStoreWall, end = '')    
                    print()
            else:
                for m in range(1,4):
                    print(mapEmpty + mapStoreName + mapStoreOwner + mapStoreWall, end = '')
                    print(28*mapEmpty, end = '')
                    print(mapEmpty + mapStoreName + mapStoreOwner + mapStoreWall)

    def getStoreName(self,data):
        storeName = ""
        if (len(data) <= 4):
            storeName = data + (4-len(data))*"　"
        return storeName

if __name__ == "__main__":
    myMap = playMap()
    myMap.printMap()