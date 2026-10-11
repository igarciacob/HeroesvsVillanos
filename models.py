from abc import ABC, abstractmethod
from datetime import datetime
#clase padre
class Personaje(ABC):
    #el identificador debe ser unico y lo asignamos con un contador que se incrementa cada vez que se crea un personaje
    num_personaje = 0
    def __init__(self,nombre,apellido,fechnac):
        Personaje.num_personaje += 1
        self.nombre = nombre
        self.apellido = apellido
        self.fechnac = fechnac
        self.id = Personaje.num_personaje
        #self.puntos = puntos

    def edad(self) -> int:
        hoy = datetime.now().date()
        #tenemos en cuenta si este año aun no ha cumplido
        edad = hoy.year - self.fechnac.year - ((hoy.month, hoy.day) < (self.fechnac.month, self.fechnac.day))
        return edad
    #Las clases hijas tienen que implementar el método
    @property
    @abstractmethod
    def puntos(self):
        pass

class Heroe(Personaje):
    def __init__(self,nombre, apellido, fechnac,  codigolimpio, biendocumentado, gitgod, arquitecto, detallista):
        super().__init__(nombre, apellido, fechnac)
        self.codigolimpio = codigolimpio
        self.biendocumentado = biendocumentado
        self.gitgod = gitgod
        self.arquitecto = arquitecto
        self.detallista = detallista

    @property
    def puntos(self) -> float:
        propCodigo = 0.5
        propDoc = 0.1
        propGit= 0.1
        propArq = 0.2
        propDet = 0.1
        total = (self.codigolimpio * propCodigo) + (self.biendocumentado * propDoc) + (self.gitgod * propGit) + (self.arquitecto * propArq) + (self.detallista*propDet)
        total = round(total,2)
        return total

    def __str__(self):
        return f"El héroe {self.nombre} {self.apellido} tiene {self.puntos} puntos y {self.edad()} años)"

class Villano(Personaje):
    def __init__(self,nombre, apellido, fechnac,  chagepeteador, entregadortardío, ausencias, hablador):
        super().__init__(nombre, apellido, fechnac)
        self.chagepeteador = chagepeteador
        self.entregadortardío = entregadortardío
        self.ausencias = ausencias
        self.hablador = hablador

    @property
    def puntos(self) -> float:
        propcha = 0.6
        proptar = 0.2
        propau = 0.1
        prophab =0.1
        total = (self.chagepeteador * propcha) + (self.entregadortardío * proptar ) + (self.ausencias + propau) + (self.hablador * prophab)
        total = round(total,2)
        return total

    def __str__(self):
        return f"El villano {self.nombre} {self.apellido} tiene {self.puntos} puntos y {self.edad()} años)"