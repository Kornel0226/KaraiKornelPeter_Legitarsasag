class JegyFoglalas:
    def __init__(self, jarat, utas_nev):
        self.jarat = jarat
        self.utas_nev = utas_nev

    def info(self):
        return f"{self.utas_nev} - {self.jarat.info()}"