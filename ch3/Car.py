class Car:
    color = ""
    mark = ""
    
    def setColor(self,color):
        self.color = color

    def setMark(self,mark):
        self.mark = mark

if __name__ == "__main__":  
    myCar = Car()
    myCar.setColor("Red")
    myCar.setMark("Benz")

    print("車子的顏色：", myCar.color)
    print("車子的品牌：", myCar.mark )
