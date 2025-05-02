# from tkinter import *

# root = Tk() # object

def m():
    return 'salam'

class Test:
    x = 50 # property
    def sayHello(self, name): # method
        return f'salam {name}'
    def sleep(self, name):
        return f'{name} is sleeping'


t1 = Test()
print(t1.x)
print(t1.sayHello("ali"))
print(t1.sleep("ali"))

t2 = Test()
print(t2.x)
print(t2.sayHello("reza"))
print(t2.sleep("saeed"))

t2.x = 60
print(t2.x)
