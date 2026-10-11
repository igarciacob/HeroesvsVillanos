import  random
from faker import Faker
from models import  Heroe , Villano
import logging
from loggingconf import init_logging
init_logging()
logger = logging.getLogger(__name__)
faker = Faker('es_ES')
heroes = []
villanos = []

#opcion 1 del menu crear Heroe
def crearHeroe():
    nombre = faker.first_name()
    apellido = faker.last_name()
    fecha= faker.date_of_birth(minimum_age = 10)
    heroe = Heroe(nombre,apellido,fecha, asignarCualidad(),
                  asignarCualidad(),asignarCualidad(), asignarCualidad(),asignarCualidad())

    nuevo_heroe = heroe.__dict__
    nuevo_heroe["edad"] = heroe.edad()
    nuevo_heroe["puntos"] = heroe.puntos
    heroes.append(nuevo_heroe)
    return heroes

def crearVillano():
    nombre = faker.first_name()
    apellido = faker.last_name()
    fecha=faker.date_of_birth(minimum_age = 10)
    villano = Villano(nombre,apellido,fecha, asignarCualidad(),
                  asignarCualidad(),asignarCualidad(), asignarCualidad())
    nuevo_villano = villano.__dict__
    nuevo_villano["edad"]= villano.edad()
    nuevo_villano["puntos"] = villano.puntos
    villanos.append(nuevo_villano)
    return villanos

def buscarPersonaje(dic,filtro, valor):
    resultados=[]
    if (filtro == "edad" or filtro =="puntos"):
        valor = int(valor)

    resultados = [p for p in dic if p.get(filtro) == valor]
    return resultados

def batallaPersonajes(heroes, villanos):
    heroe = random.choice(heroes)
    villano = random.choice (villanos)
    batalla = {
        "heroe" : heroe["nombre"] + " " + heroe["apellido"],
        "puntos_heroe": heroe["puntos"],
        "villano": villano["nombre"] + " " + villano["apellido"],
        "puntos_villano": villano["puntos"]

    }
    diff = heroe["puntos"] - villano["puntos"]
    if diff >0:
        batalla["ganador"]=heroe["nombre"] + " " +heroe["apellido"]
    elif diff < 0:
        batalla["ganador"] = villano["nombre"] + " " + villano["apellido"]
    else:
        batalla["ganador"] = "Empate"

    if  abs (diff) < 25:
        batalla["resultado"] = "Batalla justa"
    else:
        batalla["resultado"] = "Batalla desequilibrada"
    return batalla

def asignarCualidad ():

    valor = random.randint(1,100)
    return valor