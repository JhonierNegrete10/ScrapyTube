import json
from dotenv import load_dotenv
import os
from typing import List 

def flatten_list(lista_de_listas: List): 
    return [item for sublist in lista_de_listas for item in sublist ]

def read_env_variables():
    # Load .env file
    load_dotenv()

    # Get email and password
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    return email, password


# Open the JSON file
def read_json(file_name=".\data_videos\data_videos_1.json"):
    with open(file_name) as f:
        data = json.load(f)
    # Print the data
    return data


def save_data(data, file_name="data_videos.json"):
    # Open the file in write mode and write the data to it in JSON format
    with open(file_name, "w") as f:
        json.dump(data, f)
