class Pedarbozorgpedari:
    def pedarPedar(self):
        pass


class Madarbozorgpedari:
    def madarPedar(self):
        pass


class Pedarbozorgmadari:
    def pedarMadar(self):
        pass


class Madarbozorgmadari:

    def madarMadar(self):
        return "madar bozorg"


class Pedar(Pedarbozorgpedari, Madarbozorgpedari):
    pass


class Madar(Pedarbozorgmadari, Madarbozorgmadari):
    pass


class Bache(Pedar, Madar):
    pass


b1 = Bache()
print(b1.madarMadar())
