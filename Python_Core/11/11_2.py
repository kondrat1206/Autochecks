class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.x = x
        self.y = y

    @property
    def getval(self):
        return self.__x, self.__y
    
    @getval.setter
    def setval(self, x):
        self.__x = x[0]
        self.__y = x[1]
    
point = Point(1, 2)
print(point.getval)
point.setval = (3, 4)
print(point.getval)