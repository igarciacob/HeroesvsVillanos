from datetime import datetime
import os
import logging
def init_logging():
    fecha = datetime.now().strftime("%Y%m%d")
    nombrefichero= f"log/{fecha}-Heroes-Villanos.log"
    if not os.path.exists("log"):
        os.mkdir("log")
    logging.basicConfig(filename=nombrefichero, encoding='utf-8', level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

