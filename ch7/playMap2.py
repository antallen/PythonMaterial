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

        # 印出第八行
        print(7*mapLine + 34*mapEmpty + 7*mapLine)

        # 印出第九行，改自第五行
        for i in (22,8):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(myStores.getStoreData(str(22))[1]) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(myStores.getStoreData(str(8))[1]) + owner
        print(lines)

        # 印出第十行，改自第六行
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(22))[3])) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(8))[3])) + owner
        print(lines)

        # 印出第十一行，改自第七行
        po_tmp = ""
        lines = mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(22))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines = lines + po_tmp + mapWall
        po_tmp = ""
        lines = lines + 34*mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(8))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines =  lines + mapWall + po_tmp
        print(lines)

        # 印出第十二行，改自第八行
        print(7*mapLine + 34*mapEmpty + 7*mapLine)

        # 印出第十三行，改自第五行
        for i in (21,9):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(myStores.getStoreData(str(21))[1]) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(myStores.getStoreData(str(9))[1]) + owner
        print(lines)

        # 印出第十四行，改自第六行
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(21))[3])) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(9))[3])) + owner
        print(lines)

        # 印出第十五行，改自第七行
        po_tmp = ""
        lines = mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(21))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines = lines + po_tmp + mapWall
        po_tmp = ""
        lines = lines + 34*mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(9))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines =  lines + mapWall + po_tmp
        print(lines)

        # 印出第十六行，改自第八行
        print(7*mapLine + 34*mapEmpty + 7*mapLine)

        # 印出第十七行，改自第五行
        for i in (20,10):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(myStores.getStoreData(str(20))[1]) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(myStores.getStoreData(str(10))[1]) + owner
        print(lines)

        # 印出第十八行，改自第六行
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(20))[3])) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(10))[3])) + owner
        print(lines)

        # 印出第十九行，改自第七行
        po_tmp = ""
        lines = mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(20))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines = lines + po_tmp + mapWall
        po_tmp = ""
        lines = lines + 34*mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(10))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines =  lines + mapWall + po_tmp
        print(lines)

        # 印出第二十行，改自第八行
        print(7*mapLine + 34*mapEmpty + 7*mapLine)

        # 印出第二十一行，改自第五行
        for i in (19,11):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(myStores.getStoreData(str(19))[1]) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(myStores.getStoreData(str(11))[1]) + owner
        print(lines)

        # 印出第二十二行，改自第六行
        lines = ""
        lines = lines + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(19))[3])) + owner + mapWall
        lines = lines + 34*mapEmpty
        lines = lines + mapWall + mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(11))[3])) + owner
        print(lines)

        # 印出第二十三行，改自第七行
        po_tmp = ""
        lines = mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(19))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines = lines + po_tmp + mapWall
        po_tmp = ""
        lines = lines + 34*mapEmpty
        for j in range(len(userPo)):
            if (userPo[j] == str(str(11))):
                po_tmp = po_tmp + self.transferNo(str(j+1))
            else:
                po_tmp = po_tmp + mapEmpty
        po_tmp = po_tmp + mapEmpty
        lines =  lines + mapWall + po_tmp
        print(lines)

        # 印出第二十四行，改自第四行
        print(48*mapLine)

        # 印出第二十五行，改自第一行
        for i in range(18,11,-1):
            if (myStores.getStoreData(str(i))[2] == "-1"):
                owner = "　"
            else:
                owner = self.transferNo(myStores.getStoreData(str(i))[2])

            print(mapEmpty + self.getStoreName(myStores.getStoreData(str(i))[1]) + owner,end = '')
            if ((i <= 18) and ( i > 12)):
                print(mapWall,end='')
            else:
                print()
        
        # 印出第二十六行，改自第二行
        for i in range(18,11,-1):
            print(mapEmpty + self.getStoreName(self.transferNo(myStores.getStoreData(str(i))[3])) + mapEmpty,end = '')
            if ((i <= 18) and ( i > 12)):
                print(mapWall,end='')
            else:
                print()

        # 印出第二十七行，改自第三行
        po_tmp = ""
        for i in range(18,11,-1):
            po_tmp = mapEmpty
            for j in range(len(userPo)):
                if (userPo[j] == str(i)):
                    po_tmp = po_tmp + self.transferNo(str(j+1))
                else:
                    po_tmp = po_tmp + mapEmpty
            po_tmp = po_tmp + mapEmpty
            if ((i <= 18) and ( i > 12)):
               print(po_tmp + mapWall,end = '')
            else:
               print(po_tmp,end = '')
        print()

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
    userPo = ['6']
    myMap.printMap(userPo)