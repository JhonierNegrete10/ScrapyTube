# Proyecto de Web Scraping: Extracción de Información de Sitios Web

## Nombre del Proyecto: ScrapyTube

ScrapyTube es un proyecto de web scraping diseñado para extraer información específica de diferentes sitios web, como listas de reproducción de YouTube, cursos de plataformas educativas como Platzi y Udemy, y otros sitios similares. El objetivo principal de ScrapyTube es automatizar la recopilación de datos relevantes para facilitar el análisis y la organización de contenido.

## Objetivos del Proyecto

El proyecto ScrapyTube tiene los siguientes objetivos:

1. **Extracción de Datos**: Utilizar técnicas de web scraping para extraer información de sitios web seleccionados, como títulos, descripciones, enlaces y otros elementos relevantes.

2. **Automatización**: Crear un sistema automatizado que pueda recopilar datos de manera eficiente y precisa, reduciendo el tiempo y el esfuerzo necesarios para obtener la información manualmente.

3. **Análisis de Datos**: Realizar un análisis básico de los datos recopilados para identificar patrones, tendencias o insights útiles.

4. **Ampliación a Plataformas Educativas**: Extender la funcionalidad de ScrapyTube para incluir la extracción de información de cursos en plataformas educativas como Platzi y Udemy.

## Tecnologías Utilizadas

ScrapyTube utiliza las siguientes tecnologías y herramientas:

- **Python**: Lenguaje de programación principal para desarrollar el proyecto.
- **Selenium**: Utilizado para automatizar la interacción con sitios web y extraer información.
- **undetected_chromedriver**: Proporciona una solución para evitar la detección de bots al utilizar Chrome.
- **XPath**: Utilizado para identificar y seleccionar elementos específicos en el HTML de la página web.

## Estructura del Proyecto

El proyecto ScrapyTube está organizado de la siguiente manera:

1. **`main.py`**: Archivo principal que contiene el código para iniciar el proceso de web scraping y extracción de datos.

2. **`scraping_utils.py`**: Módulo que contiene funciones y utilidades relacionadas con el web scraping, como la inicialización de la conexión, la extracción de datos y el análisis.

3. **`data_analysis.ipynb`**: Cuaderno de Jupyter que demuestra el análisis básico de los datos recopilados, incluyendo visualizaciones y estadísticas.

4. **`sample_html_files/`**: Carpeta que contiene versiones más cortas de los archivos HTML de ejemplo para fines de prueba y validación.

# Estado Actual del Proyecto
Hasta el momento, ScrapyTube ha logrado extraer con éxito la información de los videos de la lista de reproducción "Ver Más Tardes" de YouTube utilizando Selenium y undetected_chromedriver. Se han identificado y utilizado los siguientes XPaths para obtener datos como la URL del video, la duración, el título y el nombre del canal:


```python
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

def find_element_and_get_attribute_or_text(
    video_element: WebElement, by_method: By, identifier: str, attribute=None
):
    try:
        element = video_element.find_element(by_method, identifier)
        return element.get_attribute(attribute) if attribute else element.text
    except Exception as e:
        return None

```
## Próximos Pasos

Los siguientes pasos planificados para ScrapyTube son:

1. **Extensión a Plataformas Educativas**: Adaptar el proyecto para extraer información de cursos en plataformas educativas como Platzi y Udemy.

2. **Mejora de la Eficiencia**: Optimizar el proceso de web scraping para aumentar la velocidad y la precisión de la extracción de datos.

3. **Interfaz de Usuario**: Desarrollar una interfaz de usuario simple para ingresar la URL del sitio web objetivo y ver los resultados de la extracción.

4. **Análisis Avanzado**: Realizar análisis más profundos de los datos extraídos, como la clasificación de contenido y la identificación de temas populares.

## Colaboración

Se invita a la comunidad a colaborar con el proyecto ScrapyTube. Si estás interesado en contribuir con código, ideas o sugerencias, por favor contacta al equipo de desarrollo a través de

 <!-- [correo electrónico](mailto:ScrapyTube@example.com). -->

---
