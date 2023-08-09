

from extract_data import iniciar_sesion,  obtener_videos, cerrar_sesion
from scraping_utils import save_data


if __name__ == "__main__":
    driver = iniciar_sesion()
    lista_reproduccion = obtener_videos(driver, n_scrolling=2)
    n = len(lista_reproduccion)
    print(n)
    for video in lista_reproduccion[n - 150 : n - 1]:
        print(video)

    cerrar_sesion(driver)
    save_data(lista_reproduccion, file_name='data_videos_prueba.json')