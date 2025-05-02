class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def sayHello(self):
        return f'salam {self.name}'
    
    def sleep(self):
        return f'{self.name} is sleeping'
    
    def introduce(self):
        return f'hi \nyour name is {self.name}\nyour age is {self.age}\nyour job is {self.job}'


p1 = Person('ali', 20, 'student')
print(p1.sayHello())
print(p1.sleep())
print(p1.introduce())

p1.name = 'reza'
print(p1.sayHello())
print(p1.sleep())
print(p1.introduce())
