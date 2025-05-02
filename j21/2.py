class Test:
    x = 50
    _z = 75
    __y = 100
    def sayHello(self):
        print(self.__y)


t1 = Test()
print(t1.x)
t1.x = 150
print(t1.x)
print(t1._z)
t1._z = 80
print(t1._z)
t1.__y = 105
print(t1.__y)
t1.sayHello()

t2 = Test()
t2.sayHello()
