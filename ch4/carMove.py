def move():
    print("汽車移動中....")

def stop():
    print("汽車停止")

def start():
    print("汽車啟動")

def maintance(color,engine,battery):
    print("更換顏色：",color)
    print("更換引擎：",engine)
    print("更換電瓶：",battery)
    print("維護完成.....")

if __name__ == "__main__":
    # 汽車維護中
    print("汽車維護中....")
    maintance("red","300","12W")
    # 啟動汽車
    start()
    # 移動汽車
    move()
    # 汽車停止
    stop()