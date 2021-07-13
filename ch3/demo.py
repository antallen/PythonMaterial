import Area
import Car

if __name__ == "__main__":

    circuleArea = Area.Area(10)
    print("圓面積：",circuleArea.getArea())

    myCar = Car.Car()
    myCar.setColor("Blue")
    myCar.setMark("BMW")

    print("車子的顏色：", myCar.color)
    print("車子的品牌：", myCar.mark )