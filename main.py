from menu import menu
import logging #registrar log
from loggingconf import init_logging
init_logging()
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        menu()

    except BaseException as e:
        logger.error( f"Se ha producido un error de aplicacion {e}")
