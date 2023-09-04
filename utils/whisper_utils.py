import logging
import pytube
import whisper
import sys
import os


def download_and_transcribe_videos(video_urls, model_name="small"):
    success_urls = []
    failed_urls = []

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    model = whisper.load_model(model_name)

    # Crear una carpeta para guardar los archivos de transcripción
    if not os.path.exists("transcriptions"):
        os.mkdir("transcriptions")
    logging.info(os.getcwd())

    for url in video_urls:
        try:
            logging.info(f"Downloading the video from YouTube: {url}")
            youtube_video = pytube.YouTube(url)
            audio = youtube_video.streams.get_audio_only()
            audio.download(filename="audio.mp3")

            logging.info("Transcribing the audio")
            if os.path.exists("audio.mp3"):
                logging.info("archivo existe")
            else:
                print("archivo NO existe")
                print(os.getcwd())
        except Exception as e:
            failed_urls.append(url)
            logging.error(f"Failed to process {url}: {str(e)}")
        # try:
        result = model.transcribe("audio.mp3")
        transcription = result["text"]
        logging.info(transcription)

        # # Crear el nombre del archivo de transcripción usando el título del video
        # file_name = f"transcriptions/{youtube_video.title}.txt"

        # # Guardar la transcripción en un archivo de texto
        # with open(file_name, "w", encoding="utf-8") as file:
        #     file.write(transcription)

        success_urls.append(url)
        logging.info(f"Transcription for {url} saved successfully")

        # except Exception as e:
        #     failed_urls.append(url)
        #     logging.error(f"Failed to process part 2 {url}: {str(e)}")

    # Guardar las URLs que fallaron en un archivo de texto
    with open("failed_urls.txt", "w") as failed_file:
        for url in failed_urls:
            failed_file.write(url + "\n")

    logging.info("Process completed.")
    return success_urls


def limpiar_url(url: str):
    # Analizar la URL
    partes = url.split("&list")
    if len(partes) > 1:
        return partes[0]
    else:
        return url
