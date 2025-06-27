from Jarat import Jarat
from datetime import date

class NemzetkoziJarat(Jarat):
    def info(self):
        ido_str = self.indulasi_ido.strftime("%Y-%m-%d %H:%M")
        return f"Járatszám: {self.jaratszam}, Cél: {self.celallomas}, Ár: {self.jegyar} Ft, Indulás: {ido_str}, Légitársaság: {self.legitarsasag.nev}"