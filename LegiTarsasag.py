import Jarat

class LegiTarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzaadas(self, jarat):
        self.jaratok.append(jarat)

    def listaz_jaratok(self):
        for jarat in self.jaratok:
            print(jarat.info())