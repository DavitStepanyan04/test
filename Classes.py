class Base:

    def __init__(self, name1, name2, name3, name4, name5):
        self.man1 = name1
        self.man2 = name2
        self.man3 = name3
        self.man4 = name4
        self.man5 = name5


class Alexandr(Base):

    def voice(self):
        print(f"{self.man1}: voxjuyn {self.man2}")


class Aram(Base):

    def voice(self):
        print(f"{self.man2}: barev {self.man1}")


class Anahit(Base):

    def voice(self):
        print(f"{self.man1}: voxjuyn {self.man3}")
        print(f"{self.man3}: barev {self.man1}")


class Irina(Base):

    def voice(self):
        print(f"{self.man1}: voxjuyn {self.man4}")
        print(f"{self.man4}: barev {self.man1}")


class Narine(Base):

    def voice(self):
        print(f"{self.man1}: voxjuyn {self.man5}")
        print(f"{self.man5}: barev {self.man1}")


alex = Alexandr("alex", "aram", "anahit", "irina", "narine")
aram = Aram("alex", "aram", "anahit", "irina", "narine")
anahit = Anahit("alex", "anahit", "anahit", "irina", "narine")
irina = Irina("alex", "aram", "anahit", "irina", "narine")
narine = Narine("alex", "aram", "anahit", "irina", "narine")
anunner = [alex, aram, anahit, irina, narine]
for i in anunner:
    i.voice()