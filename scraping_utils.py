import json
from dotenv import load_dotenv
import os


def read_env_variables():
    # Load .env file
    load_dotenv()

    # Get email and password
    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    return email, password


# Open the JSON file
def read_json():
    with open("./data_videos.json") as f:
        data = json.load(f)
    # Print the data
    print(len(data))


def save_data(data, file_name = "data_videos.json"):
    
    # Open the file in write mode and write the data to it in JSON format
    with open(file_name, "w") as f:
        json.dump(data, f)
