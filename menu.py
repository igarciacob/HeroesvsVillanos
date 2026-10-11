import logging
from loggingconf import init_logging
from gestion import crearHeroe, crearVillano, buscarPersonaje, batallaPersonajes
init_logging()
logger = logging.getLogger(__name__)
param_busqueda = ["nombre", "apellido", "edad", "puntos"]
#e
heroes  = []
villanos = []
def menu():
    global heroes, villanos
    while True:
        print("1) Crear héroe")
        print("2) Crear villano")
        print("3) Buscar Héroe")
        print("4) Buscar Villano")
        print("5) Batalla")
        print("6) Salir")
        opt = input("Elige una opción: ")

        if opt == "1":
            logger.info("Creación de héroe")
            heroes = crearHeroe()
            mostrarResultados("Héroes registrados",heroes)
        elif opt == "2":
            logger.info("Creación de villano")
            villanos = crearVillano()
            mostrarResultados("Villanos registrados",villanos)
        elif opt == "3":
            if  heroes:
                param = input("Indica el parámetro de búsqueda").lower()
                if param not in param_busqueda:
                    print("Los parámetros de búsqueda son 'Nombre', 'Apellido', 'Edad' y 'Puntos'")
                    param = input("Indica el parámetro de búsqueda")

                valor = input("Indica el valor de búsqueda")
                result = buscarPersonaje(heroes, param, valor)
                mostrarResultados("Resultado de la búsqueda",result)
            else:
                logger.warning("No hay héroes creados")
                print("No existen héroes para realizar la búsqueda")
        elif opt =="4":
            if villanos:
                param = input("Indica el parámetro de búsqueda").lower()
                if param not in param_busqueda:
                    print("Los parámetros de búsqueda son 'Nombre', 'Apellido', 'Edad' y 'Puntos'")
                    param = input("Indica el parámetro de búsqueda")

                valor = input("Indica el valor de búsqueda")
                result = buscarPersonaje(villanos, param, valor)
                mostrarResultados("Resultado de la búsqueda",result)
            else:
                logger.warning("No hay villanos creados")
                print("No existen villanos para realizar la búsqueda")

        elif opt == "5":
            if heroes and villanos:
                logger.info("Iniciamos batalla")
                resultado = batallaPersonajes(heroes,villanos)
                mostrarResultados("Resultado de la batalla", resultado)
            else:
                logger.info("No hay personajes que enfrentar")
                print ("Para iniciar la batalla debe haber al menos un héroe y un villano")
        elif opt == "6":
            logger.info("FIN EJECUCIÓN")
            print("Hasta pronto")
            break

        else:
            logger.warning("Opción de menú no válida")
            print("Opción de menú no válida")

def mostrarResultados (mensaje,col_personajes):
    if len (col_personajes) > 0:
        logger.info(f"{mensaje}: {col_personajes}")
        print(col_personajes)
    else:
        logger.info("No existen registros para los parámetros de búsqueda")
        print("No existen registros para los parámetros de búsqueda")