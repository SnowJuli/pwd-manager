from pymongo import MongoClient
from PyInquirer import prompt
import yaml

def listLogin():
    with open("config.yaml") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    address = data["location"]
    client = MongoClient(address)
    db = client["passwords"]
    dbcol = db["pwd"]

    addinfo = {"type": "input", "name": "tag", "message": "Enter the Tag: ",}

    options = prompt(addinfo)

    for x in dbcol.find({},{ "tag": options["tag"] }):
        print(x)
