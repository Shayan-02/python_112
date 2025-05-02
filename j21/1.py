class Test:
    x = 50
    _y = 100
    __z = 150

    def sayHello(self):
        print("hello")
    def _sayHello(self):
        print("hello", self.__z)
    def __sayHello(self):
        print("hello")
    def show(self):
        print(self.__z)


t1 = Test()
print(t1.x)
print(t1._y)
t1.show()


t1.sayHello()
t1._sayHello()
# t1.__sayHello()
