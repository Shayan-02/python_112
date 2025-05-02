class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def sleep(self):
        return f'{self.name} is sleeping'

    def introduce(self):
        return f"hi \nyour name is {self.name}\nyour age is {self.age}\nyour job is {self.job}"


class student(Person):
    pass


s1 = student('ali', 20, 'student')
print(s1.sleep())
print(s1.introduce())
