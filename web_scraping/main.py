
import sys
import os
# Debido al cambio de orden de las carpetas
ruta_utils = os.path.abspath(os.path.join(os.getcwd(), '..', 'utils'))
sys.path.append(ruta_utils)

from extract_data import iniciar_sesion,  obtener_videos, cerrar_sesion
from scraping_utils import save_data


if __name__ == "__main__":
    driver = iniciar_sesion()
    lista_reproduccion = obtener_videos(driver, factor_= 1)
    n = len(lista_reproduccion)
    print(n)
    print(lista_reproduccion[-1])
    cerrar_sesion(driver)
    save_data(lista_reproduccion, file_name='data_videos_prueba.json')