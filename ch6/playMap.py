import Stores

class playMap:

    def printMap(self,userPo):
        mapEmpty = "　"
        mapWall = "｜"
        mapLine = "－"
        myStores = Stores.Stores()
        # 印出第一行
        for i in range(0,7):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])

            print(mapEmpty + self.getStoreName(myStores.getStoreData(str(i))[1]) + owner,end = '')
            if (i < 6):
                print(mapWall,end='')
            else:
                print()
        # 印出第二行
        for i in range(0,7):
            print(mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(i))[3])) + mapEmpty,end = '')
            if (i < 6):
                print(mapWall,end='')
            else:
                print()

        # 印出第三行
        po_tmp = ""
        for i in range(0,7):
            po_tmp = mapEmpty
            for j in range(len(userPo)):
                if (userPo[j] == str(i)):
                    po_tmp = po_tmp + self.transferNo(str(j+1))
                else:
                    po_tmp = po_tmp + mapEmpty
            po_tmp = po_tmp + mapEmpty
            if (i < 6):
               print(po_tmp + mapWall,end = '')
            else:
               print(po_tmp,end = '')
        print()

        # 印出第四行
        print(48*mapLine)

        # 印出第五行,修改自第一行
        for i in (23,7):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(myStores.getStoreData(str(23))[1]) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(myStores.getStoreData(str(7))[1]) + owner
        print(lines)
        
        # 印出第六行，修改自第五行
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(23))[3])) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(7))[3])) + owner
        print(lines)

        # 印出第七行，修改自第三行
        po_tmp = ""
        lines = mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(23))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines = lines + po_tmp + mapWall
        po_tmp = ""
        lines = lines + 34*mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(7))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines =  lines + mapWall + po_tmp
        print(lines)

    # 控制每一行的格式大小
    def getStoreName(self,data):
        storeName = ""
        if (len(data) <= 4):
            storeName = data + (4-len(data))*"　"
        return storeName

    # 半形全形轉換功能
    def transferNo(self,data):
        nums = (0,"０",1,"１",2,"２",3,"３",4,"４",5,"５",6,"６",7,"７",8,"８",9,"９")
        tmp = []
        dataleng = len(data)
        for j in range(0,dataleng):
            tmp.append(0)

        newdata = ""
        for i in range(1,dataleng+1):
            tmp[(dataleng-i)] = int(data)%10
            data = int(int(data) / 10)

        for i in range(0,len(tmp)):
            newdata += nums[nums.index(tmp[i])+1]

        return newdata

if __name__ == "__main__":
    myMap = playMap()
    userPo = ['6','23','7','1']
    myMap.printMap(userPo)