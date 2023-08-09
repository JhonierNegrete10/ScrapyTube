import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time

from scraping_utils import read_env_variables, save_data


def iniciar_sesion():
    email, password = read_env_variables()

    options = webdriver.ChromeOptions()
    # options.add_argument('proxy-server=106.122.8.54:3128')
    # options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    browser = uc.Chrome(
        options=options,
    )

    # url = 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&hl=en&flowName=GlifWebSignIn&flowEntry=ServiceLogin'
    url = "https://accounts.google.com/v3/signin/identifier?dsh=S1896654986%3A1689754282967154&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Des-419%26next%3Dhttps%253A%252F%252Fwww.youtube.com%252F%253FthemeRefresh%253D1&ec=65620&hl=es-419&ifkv=AeDOFXiHFs-RVVcRs_XpItjNOvzJSbv6u1tJxrD5J_rcPZQg7eKW-oVFhDzGLA5rzAdpCQGU5IiT-w&passive=true&service=youtube&uilel=3&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    browser.get(url)

    browser.find_element(By.ID, "identifierId").send_keys(email)

    browser.find_element(
        By.CSS_SELECTOR, "#identifierNext > div > button > span"
    ).click()

    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"

    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector))
    )

    browser.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)

    browser.find_element(By.CSS_SELECTOR, "#passwordNext > div > button > span").click()

    time.sleep(5)
    return browser




def obtener_videos(driver: WebElement, n_scrolling = 30 ):
    videos = []

    # Espera hasta que la lista de reproducción "Ver más tarde" esté visible
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Ver más tarde")))

    # Haz clic en la lista de reproducción "Ver más tarde"
    ver_mas_tarde_link = driver.find_element(By.LINK_TEXT, "Ver más tarde")
    ver_mas_tarde_link.click()

    time.sleep(5)
    # Realiza el desplazamiento para cargar todos los videos
    for _ in range(n_scrolling):
        scroll_videos(driver)

    # Espera hasta que los videos estén cargados
    wait.until(
        EC.presence_of_all_elements_located(
            (By.TAG_NAME, "ytd-playlist-video-renderer")
        )
    )
    video_elements: list[WebElement] = driver.find_elements(
        By.TAG_NAME, "ytd-playlist-video-renderer"
    )

    # Extrae la información de los videos
    for video_element in video_elements:
        url_video = find_element_and_get_attribute_or_text(
            video_element, By.ID, "video-title1", "href"
        )
        duracion_video = find_element_and_get_attribute_or_text(
            video_element, By.CLASS_NAME, "ytd-thumbnail-overlay-time-status-renderer"
        )
        titulo_video = find_element_and_get_attribute_or_text(
            video_element, By.ID, "video-title"
        )
        nombre_canal = find_element_and_get_attribute_or_text(
            video_element, By.CSS_SELECTOR, "ytd-channel-name a"
        )

        videos.append(
            {
                "url_video": url_video,
                "duracion_video": duracion_video,
                "titulo_video": titulo_video,
                "nombre_canal": nombre_canal,
                # 'numero_vistas': numero_vistas,
                # 'tiempo_publicacion': tiempo_publicacion
            }
        )

    return videos


def cerrar_sesion(driver):
    driver.quit()


def find_element_and_get_attribute_or_text(
    video_element: WebElement, by_method: By, identifier: str, attribute=None
):
    try:
        element = video_element.find_element(by_method, identifier)
        return element.get_attribute(attribute) if attribute else element.text
    except Exception as e:
        return None


def scroll_videos(driver: WebElement):
    # Realiza desplazamiento para cargar más videos hasta que no haya más elementos
    while True:
        video_elements = driver.find_elements(
            By.TAG_NAME, "ytd-playlist-video-renderer"
        )
        driver.execute_script("arguments[0].scrollIntoView();", video_elements[-1])

        # Espera hasta que aparezcan nuevos elementos o hasta que se alcance el final de la lista
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(
                EC.presence_of_element_located(
                    (By.TAG_NAME, "ytd-playlist-video-renderer:last-child")
                )
            )
        except:
            break


if __name__ == "__main__":

    driver = iniciar_sesion()
    lista_reproduccion = obtener_videos(driver)
    n = len(lista_reproduccion)
    print(n)
    for video in lista_reproduccion[n - 150 : n - 1]:
        print(video)

    cerrar_sesion(driver)
    save_data(lista_reproduccion)

