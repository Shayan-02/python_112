class Test:
    x = 10
    _x = 10
    __x = 10
    
    def set_x(self, balance):
        self.__x = balance
    def get_x(self):
        return self.__x


t1 = Test()
print(t1.x)
print(t1._x)
# print(t1.__x)

print(t1.get_x())
t1.set_x(20)
print(t1.get_x())
