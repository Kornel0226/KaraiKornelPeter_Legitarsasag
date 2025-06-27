from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam, celallomas, jegyar, legitarsasag, indulasi_ido):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar
        self.legitarsasag = legitarsasag
        self.indulasi_ido = indulasi_ido

    @abstractmethod
    def info(self):
        pass
