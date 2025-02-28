"""
v -> no
kh -> no
"""
def test1(): 
    print("hello")


"""
v -> no
kh -> yes
"""
def test2():
    return "hello"


"""
v -> yes
kh -> no
"""
def sayHello(name):
    print("hello", name)


"""
v -> yes
kh -> yes
"""
def sayHi(mamad):
    return mamad


# calling
test1()
print(test2())
sayHello("ali")
print(sayHi("reza"))

a = sayHi(25)
print(a * 2)