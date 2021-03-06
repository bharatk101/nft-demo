import os
from pathlib import Path
import requests


PINATA_BASE_URL = "https://api.pinata.cloud/"
END_POINT = "pinning/pinFileToIPFS"

filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {"pinata_api_key": os.getenv(
    "PINATA_APIKEY"), "pinata_secret_api_key": os.getenv("PINATA_APISECRET")}


def main():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(PINATA_BASE_URL+END_POINT,
                                 files={"file": image_binary}, headers=headers)
        print(response.json())
