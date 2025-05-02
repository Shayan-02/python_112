class Test:
    x = 50
    _z = 75
    __y = 100

    def sayHello(self):
        print(self.__y)

    def sety(self, y):
        self.__y = y
    def gety(self):
        print(self.__y)


t1 = Test()
t1.gety()
t1.sety(105)
t1.gety()
