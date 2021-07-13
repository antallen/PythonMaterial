class Area:

    def __init__(self,radius):
        self.radius = radius
        self.PI = 3.141592
        self.area = 0

    def getArea(self):
        self.area = self.radius * self.radius * self.PI
        return self.area

