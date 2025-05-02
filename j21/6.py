class alive:
    def move(self):
        pass


class Person(alive):
    def move(self):
        return "walking..."


class Tarkibi(alive):
    def move(self):
        return "random"


class Fish(alive):
    def move(self):
        return "swimming..."

class Frog(Tarkibi, Fish):
    def move(self, status):
        if status == "in water":
            return "swimming"
        elif status == "out of water":
            return "sitting and jumpping"


p1 = Person()
print(p1.move())
