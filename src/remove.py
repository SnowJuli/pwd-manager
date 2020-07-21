from pymongo import MongoClient
from PyInquirer import prompt
import yaml


def removeLogin():
    with open("config.yaml") as f:
        data = yaml.safe_load(f, Loader=yaml.FullLoader)

    address = data["location"]
    client = MongoClient(address)
    db = client["passwords"]
    dbcol = db["pwd"]

    addinfo = [
        {"type": "input", "name": "tag", "message": "Enter the Tag of the Login: ",}
    ]
    options = prompt(addinfo)

    input_tag = {"tag": options["tag"]}

    dbcol.delete_one(input_tag)
    print("Login deleted.")
